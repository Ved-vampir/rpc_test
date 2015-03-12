#!/usr/bin/env python

import os
import sys
import time
import psutil
import threading

from rpc_client import remote_call

HOST = "172.16.54.71"
PORT = int(os.getenv("PORT", 39997))

class MyThread(threading.Thread):
    def run(self):
        try:
            threading.Thread.run(self)
        except Exception as self.err:
            pass # or raise
        else:
            self.err = None

class Nethogs():
    def __init__(self):
        self.log_name = "nethog.log"
        self.log_file = None
        self.net_logger = None
        self.started = False

    def start(self):
        if self.started:
            self.exit()
        self.log_file = open("nethog.log", "w")
        self.net_logger = psutil.Popen("nethogs -t -f python em1", shell=True, stdout=self.log_file)
        self.started = True

    # returns (send, recv)
    def exit(self):
        if not self.started:
            return (0, 0)
        time.sleep(3)
        pss = self.net_logger.children()
        for ps in pss:
            ps.kill()
        self.net_logger.kill()
        self.log_file.close()
        self.started = False

        total_recv = 0
        total_send = 0
        with open("nethog.log", "r") as f:
            raw = f.read()
            log = raw.split("\n")
            #print log
            for red in log:
                s = red.split("\t")
                if len(s) == 3:
                    total_recv += float(s[2])
                    total_send += float(s[1])

        return (total_send, total_recv)


def main():
    rpc_type = sys.argv[1]
    client_count = int(sys.argv[2])
    mes_size = int(sys.argv[3])

    net_logger = Nethogs()

    print "============== %s (%i clients, %i bytes) ==================" % (rpc_type, client_count, mes_size)
    print "============== reading test =================="
    print "- Single read test -"
    net_logger.start()
    begin = time.time()
    l = remote_call(host=HOST, port=PORT, rpc_type=rpc_type, read=True)
    lat = time.time() - begin
    kbytes = net_logger.exit()
    print "mes len = %f kb, time : %f sec" % (l/1024, lat)
    print "sent = %f kb, recv = %f kb" % kbytes

 
    print "- Multiple (%i) connections test -" % client_count
    net_logger.start()
    tests = []
    begin = time.time()
    for i in range(0, client_count):
        delay = client_count - i
        tests.append(MyThread(target=remote_call,
                              args=(HOST, PORT, rpc_type, True, delay)))
        tests[i].start()
    failed = 0
    for i in range(0, client_count):
        tests[i].join()
        if tests[i].err is not None:
            failed += 1

    lat = time.time() - begin
    kbytes = net_logger.exit()
    print "%i clients failed, total time : %f sec, average time : %f sec" % (failed, lat, lat/client_count)
    print "sent = %f kb, recv = %f kb" % kbytes
    print "average sent = %f kb, recv = %f kb" % (kbytes[0]/client_count, kbytes[1]/client_count)

    print "============== writing test =================="
    print "- Single write test -"
    net_logger.start()
    begin = time.time()
    l = remote_call(host=HOST, port=PORT, rpc_type=rpc_type, read=False, args="0"*mes_size)
    lat = time.time() - begin
    kbytes = net_logger.exit()
    print "mes len = %f kb, time : %f sec" % (mes_size/1024, lat)
    print "sent = %f kb, recv = %f kb" % kbytes
 
    print "- Multiple (%i) connections test -" % client_count
    net_logger.start()
    tests = []
    begin = time.time()
    for i in range(0, client_count):
        delay = client_count - i
        tests.append(MyThread(target=remote_call,
                              args=(HOST, PORT, rpc_type, False, delay, "0"*mes_size)))
        tests[i].start()
    failed = 0
    for i in range(0, client_count):
        tests[i].join()
        if tests[i].err is not None:
            failed += 1

    lat = time.time() - begin
    kbytes = net_logger.exit()
    print "%i clients failed, total time : %f sec, average time : %f sec" % (failed, lat, lat/client_count)
    print "sent = %f kb, recv = %f kb" % kbytes
    print "average sent = %f kb, recv = %f kb" % (kbytes[0]/client_count, kbytes[1]/client_count)



if __name__ == '__main__':
    main()
