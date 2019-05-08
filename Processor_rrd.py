#!/usr/bin/python3
import os
import datetime
import time
from create_rrdfiles import create_CPU
from pathlib import Path
import psutil
import subprocess
from createLogFile import createLog

def list_CPUs():
    cpus_percent_list = [] #this is a list of dictionaries where each dictionary contains a CPU
    per_cent = psutil.cpu_times_percent(interval=0.5, percpu=True)
    for cpu_num, per_cent in enumerate(per_cent):
        temp_CPU = {
            "user" : per_cent.user,
            "nice" : per_cent.nice,
            "system" : per_cent.system,
            "idle" : per_cent.idle,
            "iowait" : per_cent.iowait,
            "irq" : per_cent.irq,
            "softirq" : per_cent.softirq,
            "steal" : per_cent.steal,
            "guest" : per_cent.guest
        }
        cpus_percent_list.append(temp_CPU)
    return cpus_percent_list


def get_CPU_percent(CPU_dict, cpu_num):
    file_name = "/var/sys_monitoring/update_CPU" + str(cpu_num) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/CPU" + str(cpu_num) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd";

    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_CPU(cpu_num, str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")

    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/CPU%d_%s.rrd -t user:nice:system:idle:iowait:irq:softirq:steal:guest %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n"
          % (cpu_num, datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU_dict["user"], CPU_dict["nice"], CPU_dict["system"], CPU_dict["idle"],
             CPU_dict["iowait"],CPU_dict["irq"], CPU_dict["softirq"], CPU_dict["steal"], CPU_dict["guest"]))
    f.close()
    try: 
        subprocess.check_output("rrdtool update /var/sys_monitoring/CPU%d_%s.rrd -t user:nice:system:idle:iowait:irq:softirq:steal:guest %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n"
          % (cpu_num, datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU_dict["user"], CPU_dict["nice"], CPU_dict["system"], CPU_dict["idle"],
             CPU_dict["iowait"],CPU_dict["irq"], CPU_dict["softirq"], CPU_dict["steal"], CPU_dict["guest"]), shell=True)
    except subprocess.CalledProcessError as err: 
        createLog(str(err.returncode) + ": " + err.output + " while update CPU at " + timing)
    
def main():
    #this give a list of all the processes the system is running
     for CPU_num, CPU_dict in enumerate(list_CPUs()): #this calls the function that update each CPU in a loop for all CPU
        get_CPU_percent(CPU_dict, CPU_num)

if __name__ == '__main__':
     main()
