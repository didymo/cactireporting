import datetime
import rrdtool
import time


def graph_loadavg():
    path = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".png"
    rrdtool.graph(path, '--imgformat', 'PNG',
                  '--width', '540',
                  '--height', '100',
                  '--start', '-1d',
                  '--end', str(int(time.time())),
                  '--vertical-label', 'ms/s',
                  '--title', 'Load Average',
                  'DEF:load_1min=/var/sys_monitoring/loadavg_2019-02-26.rrd:load_1min:LAST',
                  'DEF:load_5min=/var/sys_monitoring/loadavg_2019-02-26.rrd:load_5min:LAST',
                  'DEF:load_15min=/var/sys_monitoring/loadavg_2019-02-26.rrd:load_15min:LAST',
                  'LINE1:load_1min#0000FF:Load_1min',
                  'LINE1:load_5min#004F00:Load_5min',
                  'LINE1:load_15min#000000:Load_15min')
    #print("Graph created!")

def main():
    graph_loadavg()

if __name__ == '__main__':
     main()