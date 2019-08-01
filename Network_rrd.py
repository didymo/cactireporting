#!/usr/bin/env python3
import os
import datetime
import time
import subprocess
import psutil
from pathlib import Path
from create_rrdfiles import create_Network
from createLogFile import createLog
def get_Network():
    network_interface = psutil.net_io_counters(pernic=True)
    ifaces = psutil.net_if_addrs()
    networks = list()#this is a list of dictonaries where each dict is a network
    for k, v in ifaces.items():
        ip = v[0].address
        data = network_interface[k]
        if_network = dict()
        if_network['ip'] = ip #ip address as the key
        if_network['iface'] = k #k is network name
        if_network['sent'] = data.bytes_sent/1024/1024
        if_network['recv'] = data.bytes_recv/1024/1024
        if_network['packets_sent'] = data.packets_sent
        if_network['packets_recv'] = data.packets_recv
        if_network['errin'] = data.errin
        if_network['errout'] = data.errout
        networks.append(if_network)
    return networks

def update_Network():
    networks = get_Network() #retrieve all the networks
    file_name = "/var/sys_monitoring/update_Network_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    timing = str(int(time.time()))[:-1] + "0"
    for iface in networks: #for each nic card, system will write
        file_rrd = "/var/sys_monitoring/network_" + iface['iface'] + "_"  + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd"
        try:
            check_file = open(file_rrd, 'r')
        except FileNotFoundError:
            create_Network(iface['iface'], str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")
        f.write("rrdtool update /var/sys_monitoring/network_%s_%s.rrd -t sent:recv %s:%f:%f\n"
% (iface['iface'], datetime.datetime.now().strftime('%Y-%m-%d'), timing, iface["sent"], iface["recv"]))
        try:
            subprocess.check_output("rrdtool update /var/sys_monitoring/network_%s_%s.rrd -t sent:recv %s:%f:%f\n"
        % (iface['iface'], datetime.datetime.now().strftime('%Y-%m-%d'), timing, iface["sent"], iface["recv"]), shell=True)
        except subprocess.CalledProcessError as err: 
            createLog(str(err.returncode) + ": " + str(err.output) + " while update Network at " + timing)
    f.close()

def main():
    update_Network()

if __name__ == '__main__':
    main()
