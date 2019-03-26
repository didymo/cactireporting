#!/usr/bin/env python3
import os
import sys
sys.path.append('/home/minh/PycharmProjects/Uptime-like_Information/venv/lib/python3.6/site-packages')
import datetime
import time
import rrdtool
import psutil

def create_LoadAvg():
    data_sources = ['DS:load_1min:GAUGE:60:0:U', 'DS:load_5min:GAUGE:60:0:U',
                    'DS:load_15min:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "60",
                   data_sources,"RRA:LAST:0.5:1:1440")


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

def create_Status_Processes():
    data_sources = ['DS:running:GAUGE:60:0:U', 'DS:sleeping:GAUGE:60:0:U',
                    'DS:idle:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/processes_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "60",
                   data_sources, "RRA:LAST:0.5:1:1440")

def create_Network(kname):
    data_sources_bytes = ['DS:sent:GAUGE:600:0:U', 'DS:recv:GAUGE:600:0:U']
    file_name_bytes = "/var/sys_monitoring/network_" + str(kname) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name_bytes, "--start", str(int(time.time())), "--step", "600",
                   data_sources_bytes, "RRA:LAST:0.5:1:144")

def create_Network_temp(kname):
    data_sources_bytes = ['DS:sent:GAUGE:600:0:U', 'DS:recv:GAUGE:600:0:U',
                          'DS:sent_per_sec:GAUGE:600:0:U', 'DS:recv_per_sec:GAUGE:600:0:U']
    file_name_bytes = "/var/sys_monitoring/network_temp_" + str(kname) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name_bytes, "--start", str(int(time.time())), "--step", "600",
                   data_sources_bytes, "RRA:LAST:0.5:1:144")

def main():
    #this give the avg of the computational work the system is performing in 3 intervals
    file_name = "/var/sys_monitoring/timeslogtestfile.txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    f.write("Printed Recorded at %s - %d\n" % (datetime.datetime.now(), int(time.time())))
    create_LoadAvg()
    create_Memory()
    create_Swap()
    for cpu_num in range(psutil.cpu_count()):
        create_CPU(cpu_num)
    create_Status_Processes()
    for k, v in psutil.net_if_addrs().items():
        create_Network(k)#for each nic card, a rrdfile is created
        create_Network_temp(k)

    f.write("Printed Recorded at %s - %d\n" % (datetime.datetime.now(), int(time.time())))
    f.close()

if __name__ == '__main__':
     main()
