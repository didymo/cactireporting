#!/usr/bin/python3
import os
import datetime
import time
from pathlib import Path
import subprocess
import psutil
from create_rrdfiles import create_WaitIO #NEED TO CREATE THIS IN CREATE_RRDFILES.PY
from createLogFile import createLog

def get_WaitIO():
    cpus_percent_list = [] #this is a list of dictionaries where each dictionary contains a CPU$
    per_cent = psutil.cpu_times_percent(interval=0.5, percpu=True)
    for cpu_num, per_cent in enumerate(per_cent):
        wait_CPU =  per_cent.iowait
        cpus_percent_list.append(wait_CPU)
    return cpus_percent_list

def update_WaitIO(CPU0, CPU1):
    file_name = "/var/sys_monitoring/update_WaitIO"+ "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/diskwait_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_WaitIO(str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")
    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/diskwait_%s.rrd -t CPU0:CPU1 %s:%s:%s\n"
         % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU0, CPU1))
    f.close()
    try: 
        subprocess.check_output("rrdtool update /var/sys_monitoring/diskwait_%s.rrd -t CPU0:CPU1 %s:%s:%s\n"
         % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU0, CPU1), shell=True)
    except subprocess.CalledProcessError as err: 
        createLog(str(err.returncode) + ": " + str(err.output) + " while update CPU at " + timing)

def main(): 
    update_WaitIO(get_WaitIO()[0], get_WaitIO()[1])

if __name__ == "__main__":
    main()
