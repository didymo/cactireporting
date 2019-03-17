# System Reporting 

Prerequisite
Python 3.6 
PyCharm 1.13.4801
psutil 5.5.1 (a cross-platform library aiding in retrieving information regarding running processes and system utilities)
python-rrdtool 


Installation 
psutil: https://github.com/giampaolo/psutil/blob/master/INSTALL.rst
rrdtool: https://pythonhosted.org/rrdtool/install.html#debian-ubuntu

Edit crontab (under root):
# at every minute of the day 
* * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/LoadAvg_rrd.py
* * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Processes_rrd.py

#at every 5 minutes of the day 
*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Memory_rrd.py
*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Processor_rrd.py

# at every 12:00am of everyday 
0 0 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdfiles.py

#at every 23:59 of everyday, create the report of the day today 
59 23 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdgraphs.py
