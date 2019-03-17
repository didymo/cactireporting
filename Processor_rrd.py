#!/usr/bin/python3

import os
import datetime
import time
from pathlib import Path
import psutil

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
    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/CPU%d_%s.rrd -t user:nice:system:idle:iowait:irq:softirq:steal:guest %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n"
          % (cpu_num, datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU_dict["user"], CPU_dict["nice"], CPU_dict["system"], CPU_dict["idle"],
             CPU_dict["iowait"],CPU_dict["irq"], CPU_dict["softirq"], CPU_dict["steal"], CPU_dict["guest"]))
    f.close()
    os.system("rrdtool update /var/sys_monitoring/CPU%d_%s.rrd -t user:nice:system:idle:iowait:irq:softirq:steal:guest %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n"
          % (cpu_num, datetime.datetime.now().strftime('%Y-%m-%d'), timing, CPU_dict["user"], CPU_dict["nice"], CPU_dict["system"], CPU_dict["idle"],
             CPU_dict["iowait"],CPU_dict["irq"], CPU_dict["softirq"], CPU_dict["steal"], CPU_dict["guest"]))

def main():
    #this give a list of all the processes the system is running
     for CPU_num, CPU_dict in enumerate(list_CPUs()): #this calls the function that update each CPU in a loop for all CPU
        get_CPU_percent(CPU_dict, CPU_num)

if __name__ == '__main__':
     main()
