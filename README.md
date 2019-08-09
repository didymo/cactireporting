--------------Environment-------------
- Python3 
- Pillow (PIL support for Python3) 




----------- CRONTAB ------------------

# at 5 a.m every week with:
# at every minute of the day 
* * * * * python3 /LoadAvg_rrd.py
* * * * * python3 /Processes_rrd.py
* * * * * python3 /DiskIO_rrd.py

#at every 5 minutes of the day 
5 * * * * python3 /Memory_rrd.py
5 * * * * python3 /Processor_rrd.py
5 * * * * python3 /Network_rrd.py

#at every 23:59 of everyday, create the report of the day today + create rrd files for next day
0 0 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdfiles.py
59 23 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdgraphs.py


# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

