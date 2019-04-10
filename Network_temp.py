#!/usr/bin/env python3
import os
import datetime
import time
import psutil
from pathlib import Path
from create_rrdfiles import create_Network_temp

def get_Network():
    #Before
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)
    #print(tot_before)
    #print(pnic_before)

    #sleep some interval so we can compute rates
    interval = 0.2
    time.sleep(interval)

    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)
    #print("Total bytes:")
    #print("Sent: %s" % tot_after.bytes_sent)
    #print("Received: %s" % tot_after.bytes_recv)

    nic_names = list(pnic_after.keys())#each interface is identified by their name
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)
    nic_list = list()
    #this is the interface
    for name in nic_names:
        nic = dict()
        nic['name'] = name
        stats_before = pnic_before[name]
        stats_after = pnic_after[name]
        nic['sent'] = stats_after.bytes_sent
        nic['sent_per_sec'] = stats_after.bytes_sent - stats_before.bytes_sent
        nic['recv'] = stats_after.bytes_recv
        nic['recv_per_sec'] = stats_after.bytes_recv - stats_before.bytes_recv
        nic['packets_sent'] = stats_after.packets_sent
        nic['packets_sent_per_sec'] = stats_after.packets_sent - stats_before.packets_sent
        nic['packets_recv'] = stats_after.packets_recv
        nic['pactket_recv_per_sec'] = stats_after.packets_recv - stats_before.packets_recv
        nic_list.append(nic)
    return nic_list

def update_Network():
    nic_list = get_Network()
    file_name = "/var/sys_monitoring/update_Network_temp_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".txt"
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")
    timing = str(int(time.time()))[:-1] + "0"
    for nic in nic_list:  # for each nic card, system will write
        file_rrd = "/var/sys_monitoring/network_temp_" + nic['name'] + "_"  + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd";

        try:
            check_file = open(file_rrd, 'r')
        except FileNotFoundError:
            create_Network_temp(nic['name'], str(int(time.time()) - 60)[:-1] + "0")  # create a file 60sec before so its updating
        f.write("TEMPORARY CREATED at "+ str(int(time.time()) - 60)[:-1] + "0" +  " 60 seconds before " + str(int(time.time()))[:-1] +"0" + "\n")

        f.write("rrdtool update /var/sys_monitoring/network_temp_%s_%s.rrd -t sent:recv:sent_per_sec:recv_per_sec %s:%f:%f:%f:%f\n"
                % (nic['name'], datetime.datetime.now().strftime('%Y-%m-%d'), timing, nic["sent"], nic["recv"],
                   nic['sent_per_sec'], nic['recv_per_sec']))
        os.system("rrdtool update /var/sys_monitoring/network_temp_%s_%s.rrd -t sent:recv:sent_per_sec:recv_per_sec %s:%f:%f:%f:%f\n"
            % (nic['name'], datetime.datetime.now().strftime('%Y-%m-%d'), timing, nic["sent"], nic["recv"],
               nic['sent_per_sec'], nic['recv_per_sec']))
    f.close()

def main():
    update_Network()

if __name__ == '__main__':
    main()
