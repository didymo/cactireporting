import datetime
import rrdtool
import time


def graph_loadavg():
    path = "/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".png"
    def1 = "DEF:load_1min=/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:load_1min:LAST"
    def2 = "DEF:load_5min=/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:load_5min:LAST"
    def3 = "DEF:load_15min=/var/sys_monitoring/loadavg_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:load_15min:LAST"
    rrdtool.graph(path, '--imgformat', 'PNG',
                  '--width', '1274',
                  '--height', '346',
                  '--start', '-1d',
                  '--end', str(int(time.time())),
                  '--vertical-label', 'ms/s',
                  '--title', 'Load Average', def1, def2, def3,
                  'LINE1:load_1min#0000FF:Load_1min',
                  'LINE1:load_5min#004F00:Load_5min',
                  'LINE1:load_15min#ff69b4:Load_15min')
    #print("Graph created!")

def main():
    graph_loadavg()

if __name__ == '__main__':
     main()
