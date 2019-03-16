#!/usr/bin/env python3
import os
import sys
sys.path.append('/home/minh/PycharmProjects/Uptime-like_Information/venv/lib/python3.6/site-packages')
import datetime
import time
import rrdtool
import psutil

def create_LoadAvg():
    data_sources = ['DS:load_1min:GAUGE:600:0:U', 'DS:load_5min:GAUGE:60:0:U',
                    'DS:load_15min:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "60",
                   data_sources,"RRA:LAST:0.5:1:1440")

def create_each_CPU():
    cpu_num = psutil.cpu_count()
    data_sources = []
    for i in range(cpu_num):
        ds_name = "CPU" + str(i)
        data_sources.append('DS:' + ds_name + ':GAUGE:600:0:U')
    file_name = "/var/sys_monitoring/CPUs_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "600",
                   data_sources,"RRA:LAST:0.5:1:144")

def create_Memory():
    data_sources = ['DS:used:GAUGE:600:0:U', 'DS:percent:GAUGE:600:0:U',
                    'DS:active:GAUGE:600:0:U', 'DS:inactive:GAUGE:600:0:U',
                    'DS:buffers:GAUGE:600:0:U', 'DS:cached:GAUGE:600:0:U',
                    'DS:available:GAUGE:600:0:U', 'DS:free:GAUGE:600:0:U',
                    'DS:shared:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "600",
                   data_sources,"RRA:LAST:0.5:1:144")

def create_Swap():
    data_sources = ['DS:total:GAUGE:600:0:U', 'DS:used:GAUGE:600:0:U',
                    'DS:free:GAUGE:600:0:U', 'DS:percent:GAUGE:600:0:U',
                    'DS:sin:GAUGE:600:0:U', 'DS:sout:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "600",
                   data_sources, "RRA:LAST:0.5:1:144")

def create_CPU(cpu_num):
    data_sources = ['DS:user:GAUGE:600:0:U', 'DS:nice:GAUGE:600:0:U',
                    'DS:system:GAUGE:600:0:U', 'DS:idle:GAUGE:600:0:U',
                    'DS:iowait:GAUGE:600:0:U', 'DS:irq:GAUGE:600:0:U',
                    'DS:softirq:GAUGE:600:0:U', 'DS:steal:GAUGE:600:0:U',
                    'DS:guest:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/CPU" + str(cpu_num) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "600",
                   data_sources, "RRA:LAST:0.5:1:144")

def main():
    #this give the avg of the computational work the system is performing in 3 intervals
    create_LoadAvg()
    create_Memory()
    create_Swap()
    for cpu_num in range(psutil.cpu_count()):
        create_CPU(cpu_num)

if __name__ == '__main__':
     main()
