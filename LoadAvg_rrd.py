#!/usr/bin/env python3
import os
import datetime
import time
from pathlib import Path
from create_rrdfiles import create_LoadAvg

def getLoadAvg():
    load_avg = os.getloadavg()  # this results in tuplpe of 3 values loadavg_1min loadavg_5mins loadavg_15mins
    file_name = "/var/sys_monitoring/update_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    file_rrd = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd";

    try:
        check_file = open(file_rrd, 'r')
    except FileNotFoundError:
        create_LoadAvg(str(int(time.time()) - 60))  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED")
    timing = str(int(time.time()))[:-1] + "0"
    f.write("rrdtool update /var/sys_monitoring/loadavg_%s.rrd -t load_1min:load_5min:load_15min %s:%.2f:%.2f:%.2f\n"
          % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, load_avg[0], load_avg[1], load_avg[2]))
    f.close()

    os.system("rrdtool update /var/sys_monitoring/loadavg_%s.rrd -t load_1min:load_5min:load_15min %s:%.2f:%.2f:%.2f\n"
          % (datetime.datetime.now().strftime('%Y-%m-%d'), timing, load_avg[0], load_avg[1], load_avg[2]))

def main():
    #this give the avg of the computational work the system is performing in 3 intervals
    getLoadAvg()

if __name__ == '__main__':
     main()