#!/usr/bin/python3
import os

def createLog(newThing):     
    file_name = "/var/sys_monitoring/logfile.txt "
    if os.path.isfile(file_name):
        f = open(file_name, "a+")
    else:
        f = open(file_name, "w+")

    f.write(newThing + "\n")

def main(): 
    createLog("Log")

if __name__ == '__main__':
    main()
