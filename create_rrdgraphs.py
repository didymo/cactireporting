import datetime
import rrdtool
import time
import psutil


def graph_LoadAvg():
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

def graph_Memory():
    path = "/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".png"
    def1 = "DEF:used=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:used:LAST"
    def2 = "DEF:percent=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:percent:LAST"
    def3 = "DEF:active=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:active:LAST"
    def4 = "DEF:inactive=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:inactive:LAST"
    def5 = "DEF:buffers=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:buffers:LAST"
    def6 = "DEF:cached=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:cached:LAST"
    def7 = "DEF:available=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:available:LAST"
    def8 = "DEF:free=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:free:LAST"
    def9 = "DEF:shared=/var/sys_monitoring/memory_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:shared:LAST"
    rrdtool.graph(path, '--imgformat', 'PNG',
                  '--width', '1274',
                  '--height', '346',
                  '--start', '-1d',
                  '--end', str(int(time.time())),
                  '--vertical-label', 'bytes',
                  '--title', 'Memory Allocation',
                  def1, def2, def3, def4, def5, def6, def7, def8, def9,
                  'AREA:used#e6194B:used',
                  'LINE1:percent#42d4f4:percent',
                  'AREA:active#3cb44b:active:STACK',
                  'AREA:inactive#f032e6:inactive:STACK',
                  'AREA:buffers#ffe119:buffers:STACK',
                  'AREA:cached#4363d8:cached:STACK',
                  'AREA:available#a9a9a9:available:STACK',
                  'AREA:free#ffffff:free:STACK',
                  'AREA:shared#911eb4:shared:STACK')

def graph_Swap():
    path = "/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".png"
    def1 = "DEF:total=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:total:LAST"
    def2 = "DEF:used=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:used:LAST"
    def3 = "DEF:free=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:free:LAST"
    def4 = "DEF:percent=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:percent:LAST"
    def5 = "DEF:sin=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:sin:LAST"
    def6 = "DEF:sout=/var/sys_monitoring/swap_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:sout:LAST"
    rrdtool.graph(path, '--imgformat', 'PNG',
                  '--width', '1274',
                  '--height', '346',
                  '--start', '-1d',
                  '--end', str(int(time.time())),
                  '--vertical-label', 'bytes',
                  '--title', 'Swap Memory Allocation',
                  def1, def2, def3, def4, def5, def6,
                  'AREA:total#a9a9a9:total',
                  'AREA:used#e6194B:used:STACK',
                  'AREA:free#ffffff:free:STACK',
                  'LINE1:percent#000000:percent',
                  'AREA:sin#ffe119:sin:STACK',
                  'AREA:sout#4363d8:sout:STACK')

def graph_CPU(cpu_num):
    cpu_name = "CPU" + str(cpu_num)
    path = "/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".png"
    def1 = "DEF:user=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:user:LAST"
    def2 = "DEF:nice=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:nice:LAST"
    def3 = "DEF:system=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:system:LAST"
    def4 = "DEF:idle=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:idle:LAST"
    def5 = "DEF:iowait=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:iowait:LAST"
    def6 = "DEF:irq=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:irq:LAST"
    def7 = "DEF:softirq=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:softirq:LAST"
    def8 = "DEF:steal=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:steal:LAST"
    def9 = "DEF:guest=/var/sys_monitoring/" + cpu_name + "_" + datetime.datetime.now().strftime('%Y-%m-%d') + ".rrd:guest:LAST"
    rrdtool.graph(path, '--imgformat', 'PNG',
                  '--width', '1274',
                  '--height', '346',
                  '--start', '-1d',
                  '--end', str(int(time.time())),
                  '--vertical-label', 'percent',
                  '--title', 'Processors Usage',
                  def1, def2, def3, def4, def5, def6, def7, def8, def9,
                  'AREA:user#e6194B:user',
                  'AREA:nice#42d4f4:nice:STACK',
                  'AREA:system#3cb44b:system:STACK',
                  'AREA:idle#f032e6:idle:STACK',
                  'AREA:iowait#ffe119:iowait:STACK',
                  'AREA:irq#4363d8:irq:STACK',
                  'AREA:softirq#a9a9a9:softirq:STACK',
                  'AREA:steal#800000:steal:STACK',
                  'AREA:guest#911eb4:guest:STACK')

def main():
    graph_LoadAvg()
    graph_Memory()
    graph_Swap()
    for cpu_num in range(psutil.cpu_count()):
       graph_CPU(cpu_num)


if __name__ == '__main__':
     main()