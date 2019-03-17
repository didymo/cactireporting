#!/usr/bin/env python3
import os
import datetime
import time
import psutil
from pathlib import Path

def get_Network():
    #Before
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)
    print(tot_before)
    print(pnic_before)

    #sleep some interval so we can compute rates
    interval = 0.5
    time.sleep(interval)

    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)
    print("Total bytes:")
    print("Sent: %s" % tot_after.bytes_sent)
    print("Received: %s" % tot_after.bytes_recv)

    nic_names = list(pnic_after.keys())#each interface is identified by their name
    nic_names.sort(key=lambda x: sum(pnic_after[x]), reverse=True)

    #this is the interface
    for name in nic_names:
        stats_before = pnic_before[name]
        stats_after = pnic_after[name]
        print(name)
        print("Bytes-sent: %s (total) %s B/s (per-sec)" % (stats_after.bytes_sent,
                                    stats_after.bytes_sent - stats_before.bytes_sent))
        print("Bytes-recv: %s (total) %s B/s (per-sec)" % (stats_after.bytes_recv,
                                    stats_after.bytes_recv - stats_before.bytes_recv))
        print("Packets-sent: %s (total) %s/s" % (stats_after.packets_sent,
                                    stats_after.packets_sent - stats_before.packets_sent))
        print("Packets-recv: %s (total) %s/s" % (stats_after.packets_recv,
                                    stats_after.packets_recv - stats_before.packets_recv))

def main():
    get_Network()

if __name__ == '__main__':
    main()
