#!/usr/bin/env python

import sys
import time
import os
import web
from rpc import SomeRemoteClass_Web
from rpyc.utils.server import ThreadedServer
import Pyro4

import rpc

HOST = "172.16.54.71"
PORT = int(os.getenv("PORT", 39997))

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def start_grpc_server():
    import rpc_test_pb2
    server = rpc_test_pb2.early_adopter_create_SomeRemoteClass_server(rpc.SomeRemoteClass_gRpc(), PORT, None, None)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

def start_pyro_server():
    obj = rpc.SomeRemoteClass_Pyro()
    daemon = Pyro4.Daemon(host=HOST, port=PORT)
    uri = daemon.register(obj, "test.RPC")
    print "Server running, uri = %s" % uri
    daemon.requestLoop()

def start_rpyc_server():
    t = ThreadedServer(rpc.SomeRemoteClass_Rpyc, hostname=HOST, port=PORT)
    t.start()

def start_web_server():
    urls = ('/giveme', 'SomeRemoteClass_Web')
    sys.argv[1] = HOST+":"+str(PORT)
    app = web.application(urls, globals())
    app.run()



def main():
    if sys.argv[1] == "pyro":
        start_pyro_server()
    elif sys.argv[1] == "rpyc":
        start_rpyc_server()
    elif sys.argv[1] == "grpc":
        start_grpc_server()
    elif sys.argv[1] == "web":
        start_web_server()


if __name__ == '__main__':
    main()
