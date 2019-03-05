#!/usr/bin/env python3
import os
import sys
sys.path.append('/home/minh/PycharmProjects/Uptime-like_Information/venv/lib/python3.6/site-packages')
import datetime
import time
import rrdtool

def createFile():
    data_sources = ['DS:load_1min:GAUGE:60:0:U', 'DS:load_5min:GAUGE:60:0:U',
                    'DS:load_15min:GAUGE:60:0:U']
    file_name = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
    rrdtool.create(file_name, "--start", str(int(time.time())), "--step", "60",
                   data_sources,"RRA:LAST:0.5:1:1440")

def main():
    #this give the avg of the computational work the system is performing in 3 intervals
    createFile()


if __name__ == '__main__':
     main()
