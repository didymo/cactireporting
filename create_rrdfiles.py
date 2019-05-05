#!/usr/bin/env python3
import os
import sys
sys.path.append('/home/minh/PycharmProjects/Uptime-like_Information/venv/lib/python3.6/site-packages')
import datetime
import time
import rrdtool
import psutil
from createLogFile import createLog

def create_LoadAvg(time_create):
    data_sources = ['DS:load_1min:GAUGE:60:0:U', 'DS:load_5min:GAUGE:60:0:U',
                    'DS:load_15min:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", time_create, "--step", "60",
                   data_sources,"RRA:LAST:0.5:1:1440")
    createLog("Created " + file_name)

def create_Memory(time_create):
    data_sources = ['DS:used:GAUGE:600:0:U', 'DS:percent:GAUGE:600:0:U',
                    'DS:active:GAUGE:600:0:U', 'DS:inactive:GAUGE:600:0:U',
                    'DS:buffers:GAUGE:600:0:U', 'DS:cached:GAUGE:600:0:U',
                    'DS:available:GAUGE:600:0:U', 'DS:free:GAUGE:600:0:U',
                    'DS:shared:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", time_create, "--step", "600",
                   data_sources,"RRA:LAST:0.5:1:144")
    createLog("Created " + file_name)

def create_Swap(time_create):
    data_sources = ['DS:total:GAUGE:600:0:U', 'DS:used:GAUGE:600:0:U',
                    'DS:free:GAUGE:600:0:U', 'DS:percent:GAUGE:600:0:U',
                    'DS:sin:GAUGE:600:0:U', 'DS:sout:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", time_create, "--step", "600",
                   data_sources, "RRA:LAST:0.5:1:144")
    createLog("Created " + file_name)

def create_CPU(cpu_num, time_create):
    data_sources = ['DS:user:GAUGE:600:0:U', 'DS:nice:GAUGE:600:0:U',
                    'DS:system:GAUGE:600:0:U', 'DS:idle:GAUGE:600:0:U',
                    'DS:iowait:GAUGE:600:0:U', 'DS:irq:GAUGE:600:0:U',
                    'DS:softirq:GAUGE:600:0:U', 'DS:steal:GAUGE:600:0:U',
                    'DS:guest:GAUGE:600:0:U']
    file_name = "/var/sys_monitoring/CPU" + str(cpu_num) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", time_create, "--step", "600",
                   data_sources, "RRA:LAST:0.5:1:144")
    createLog("Created " + file_name)

def create_Status_Processes(time_create):
    data_sources = ['DS:running:GAUGE:60:0:U', 'DS:sleeping:GAUGE:60:0:U',
                    'DS:idle:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/processes_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", time_create, "--step", "60",
                   data_sources, "RRA:LAST:0.5:1:1440")
    createLog("Created " + file_name)

def create_Network(kname, time_create):
    data_sources_bytes = ['DS:sent:GAUGE:600:0:U', 'DS:recv:GAUGE:600:0:U']
    file_name_bytes = "/var/sys_monitoring/network_" + str(kname) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name_bytes, "--start", time_create, "--step", "600",
                   data_sources_bytes, "RRA:LAST:0.5:1:144")
    createLog("Created " + file_name_bytes)

def create_Network_temp(kname, time_create):
    data_sources_bytes = ['DS:sent:GAUGE:600:0:U', 'DS:recv:GAUGE:600:0:U',
                          'DS:sent_per_sec:GAUGE:600:0:U', 'DS:recv_per_sec:GAUGE:600:0:U']
    file_name_bytes = "/var/sys_monitoring/network_temp_" + str(kname) + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name_bytes, "--start", time_create, "--step", "600",
                   data_sources_bytes, "RRA:LAST:0.5:1:144")
    createLog("Created " + file_name_bytes)

def create_Disk_Storage(time_create):
    data_sources_bytes = ['DS:used:GAUGE:600:0:U', 'DS:free:GAUGE:600:0:U',
                          'DS:total:GAUGE:600:0:U']
    file_name_bytes = "/var/sys_monitoring/disk_storage_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name_bytes, "--start", time_create, "--step", "600",
                   data_sources_bytes, "RRA:LAST:0.5:1:144")
    createLog("Created " + file_name_bytes)

def main():
    create_LoadAvg(str(int(time.time())))
    create_Memory(str(int(time.time())))
    create_Swap(str(int(time.time())))
    #for cpu_num in range(psutil.cpu_count()):
    #    create_CPU(cpu_num, str(int(time.time())))
    #create_Status_Processes(str(int(time.time())))
    #for k, v in psutil.net_if_addrs().items():
    #    create_Network(k, str(int(time.time())))#for each nic card, a rrdfile is created
    #    create_Network_temp(k, str(int(time.time())))


if __name__ == '__main__':
     main()
