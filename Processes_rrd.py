#!/usr/bin/env python3
import os
import datetime
import time
import psutil
from pathlib import Path
from create_rrdfiles import create_Status_Processes
from createLogFile import createLog
import subprocess
import csv

#this script is counting the number of running and sleeping processes

def find_Processes_Status():
    processes_list = [] #create an empty list to store all the process as dict
    for proc in psutil.process_iter():
        try:
            process_dict = proc.as_dict(attrs=['pid', 'name', 'username', 'status'])
            process_dict['mem_usage'] = proc.memory_info().vms/(1024*1024) #add attribute memory usage to process
            processes_list.append(process_dict)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    processes_list = sorted(processes_list, key=lambda procObj: procObj['mem_usage'], reverse=True)
    #feeding the list to function that write instead of returning to avoid security issues
    store_Processes(processes_list)

def store_Processes(list_processes):
    # categorise them into 3 groups: running + sleeping + idle
    running_list = list(filter(lambda proc: proc['status'] in 'running', list_processes))
    sleeping_list = list(filter(lambda proc: proc['status'] in 'sleeping', list_processes))
    idle_list = list(filter(lambda proc: proc['status'] in 'idle', list_processes))

    get_Running_Sleeping_Idle(len(list(running_list)), len(list(sleeping_list)), len(list(idle_list)))
    csv_running = "/var/sys_monitoring/running_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".csv"
    csv_sleeping = "/var/sys_monitoring/sleeping_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".csv"
    csv_idle = "/var/sys_monitoring/idle_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".csv"

    write_Running_Sleeping_Idle(running_list, csv_running)
    write_Running_Sleeping_Idle(sleeping_list, csv_sleeping)
    write_Running_Sleeping_Idle(idle_list, csv_idle)

def get_Running_Sleeping_Idle(running, sleeping, idle):
    file_name = "/var/sys_monitoring/update_processes_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/processes_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd";

    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_Status_Processes(str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")

    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/processes_%s.rrd -t running:sleeping:idle %s:%d:%d:%d\n"
        % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, running, sleeping, idle))
    try: 
        subprocess.check_output("rrdtool update /var/sys_monitoring/processes_%s.rrd -t running:sleeping:idle %s:%d:%d:%d\n"
        % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, running, sleeping, idle))
    except subprocess.CalledProcessError as err: 
        createLog(str(err.returncode) + ": " + err.output + " while update CPU at " + timing)

def write_Running_Sleeping_Idle(list_processes, csv_path):
    try:
        with open(csv_path, 'w') as csvfile:
            field_names = ['status', 'name', 'pid', 'username', 'mem_usage']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for proc in list_processes:
                writer.writerow(proc)
    except IOError:
        print("I/O Error")

def main():
    find_Processes_Status()

if __name__ == '__main__':
    main()
