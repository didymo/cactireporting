#!/usr/bin/python3

import os
import datetime
import time
from pathlib import Path
import psutil
import subprocess
from create_rrdfiles import create_Memory
from create_rrdfiles import create_Swap
from createLogFile import createLog

def virtual_memory():
    mem = psutil.virtual_memory()
    memory_dict = {
        "total" : mem.total/1024/1024,
        "available" : mem.available/1024/1024,
        "used" : mem.used /1024/2014,
        "free" : mem.free/1024/1024,
        "percent" : mem.percent,
        "active" : mem.active/1024/1024,
        "inactive" : mem.inactive/1024/1024,
        "buffers" : mem.buffers/1024/1024,
        "cached" : mem.cached/1024/1024,
        "shared" : mem.shared/1024/1024
    }
    return memory_dict

def get_Memory ():
    file_name = "/var/sys_monitoring/update_memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd";

    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_Memory(str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")

    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/memory_%s.rrd -t used:percent:active:inactive:buffers:cached:available:free:shared %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n"
          % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, virtual_memory()["used"], virtual_memory()['percent'], virtual_memory()["active"],
             virtual_memory()["inactive"], virtual_memory()["buffers"], virtual_memory()["cached"], virtual_memory()['available'], virtual_memory()['free'],
             virtual_memory()['shared']))
    f.close()

    try: 
        subprocess.check_output("rrdtool update /var/sys_monitoring/memory_%s.rrd -t used:percent:active:inactive:buffers:cached:available:free:shared %s:%s:%s:%s:%s:%s:%s:%s:%s:%s\n" % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, virtual_memory()["used"], virtual_memory()["percent"], virtual_memory()["active"], virtual_memory()["inactive"], virtual_memory()["buffers"], virtual_memory()["cached"], virtual_memory()["available"], virtual_memory()["free"], virtual_memory()["shared"]), shell=True)
    except subprocess.CalledProcessError as err: 
        createLog(str(err.returncode) + ": " + str(err.output) + " while update Memory at " + timing)
        
def swap_memory():
    swap = psutil.swap_memory()
    swap_dict = {
        "total" : swap.total/1024/1024,
        "used" : swap.used/1024/1024,
        "free" : swap.free/1024/1024,
        "percent" : swap.percent,
        "sin" : swap.sin/1024/1024,
        "sout" : swap.sout/1024/1024
    }
    return swap_dict

def get_Swap():
    file_name = "/var/sys_monitoring/update_swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"

    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_Swap(str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")

    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/swap_%s.rrd -t total:used:free:percent:sin:sout %s:%s:%s:%s:%s:%s:%s\n"
          % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, swap_memory()["total"], swap_memory()["used"], swap_memory()["free"], swap_memory()["percent"], swap_memory()["sin"], swap_memory()["sout"]))
    f.close()
    try: 
        subprocess.check_output("rrdtool update /var/sys_monitoring/swap_%s.rrd -t total:used:free:percent:sin:sout %s:%s:%s:%s:%s:%s:%s\n" % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, swap_memory()["total"], swap_memory()["used"], swap_memory()["free"], swap_memory()["percent"], swap_memory()["sin"], swap_memory()["sout"]), shell=True)
    except subprocess.CalledProcessError as err: 
        createLog(str(err.returncode) + ": " + str(err.output) + " while update Swap at " + timing)

    
def main():
    get_Memory()
    get_Swap()

if __name__ == '__main__':
     main()
