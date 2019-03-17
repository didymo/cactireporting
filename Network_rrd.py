#!/usr/bin/env python3
import os
import datetime
import time
import psutil
from pathlib import Path

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
        if_network['sent'] = '%.2fMB' % (data.bytes_sent/1024/1024)
        if_network['recv'] = '%.2fMB' % (data.bytes_recv/1024/1024)
        if_network['packets_sent'] = data.packets_sent
        if_network['packets_recv'] = data.packets_recv
        if_network['errin'] = data.errin
        if_network['errout'] = data.errout
        networks.append(if_network)
        print(if_network)

    return networks

def main():
    get_Network()

if __name__ == '__main__':
    main()
