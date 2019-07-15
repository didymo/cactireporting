# cactireporting
# at 5 a.m every week with:
0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# at every minute of the day 
* * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/LoadAvg_rrd.py
* * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Processes_rrd.py

#at every 5 minutes of the day 
*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Memory_rrd.py
*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Processor_rrd.py
*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Network_rrd.py
#*/5 * * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/Network_temp_rrd.py

# at every 12:00am of everyday 
0 0 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdfiles.py

#at every 23:59 of everyday, create the report of the day today 
59 23 * * * python3 /home/minh/PycharmProjects/Uptime-like_Information/venv/create_rrdgraphs.py

# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
