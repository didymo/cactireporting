# System Reporting 

Prerequisite
Python 3.6 
PyCharm 1.13.4801
psutil 5.5.1 (a cross-platform library aiding in retrieving information regarding running processes and system utilities)
rrdtool 0.0.7 (PyRRD is an object-oriented wrapper for the command line graphing and round-robin database utility, rrdtool)


Installation 
psutil: https://github.com/giampaolo/psutil/blob/master/INSTALL.rst
rrdtool: https://pythonhosted.org/rrdtool/install.html#debian-ubuntu

Edit crontab (under root):
At 12:00am everyday: create a rrd file 
0 0 * * * python3 /path/to/file/generateDailyReport.py 

At 11:59pm everyday: generate a graph based on that day's data in rra 
59 23 * * * python3 /path/to/file/graph_rrd.py 

At every minute of everyday 
* * * * * python3 /path/to/file/Uptime-like_Info.py 


