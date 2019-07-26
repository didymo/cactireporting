# at 5 a.m every week with:
# at every minute of the day 
* * * * * python3 /LoadAvg_rrd.py
* * * * * python3 /Processes_rrd.py
* * * * * python3 /DiskIO_rrd.py

#at every 5 minutes of the day 
5 * * * * python3 /Memory_rrd.py
5 * * * * python3 /Processor_rrd.py
5 * * * * python3 /Network_rrd.py

# at every 12:00am of everyday 
0 0 * * * python3 /create_rrdfiles.py

#at every 23:59 of everyday, create the report of the day today 
59 23 * * * python3 /create_rrdgraphs.py

# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

