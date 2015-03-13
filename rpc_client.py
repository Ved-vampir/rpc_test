#!/usr/bin/env python

import zmq
import time
import Pyro4
import rpyc
import urllib2
# import rpc_test_pb2

_TIMEOUT_SECONDS = 10

class WebRemote(object):
    def __init__(self, host, port):
        self.read_url = "http://%s:%i/giveme" % (host, port)

    def giveme(self):
        response = urllib2.urlopen(self.read_url).read()
        return response

    def getit(self, args):
        pass

class ZeroMQRemote(object):
    def __init__(self, host, port):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://%s:%i" % (host, port))

    def giveme(self):
        self.socket.send("giveme")
        return self.socket.recv()

    def getit(self, args):
        self.socket.send(args)
        self.socket.recv()


def remote_call(host, port, rpc_type, read, delay=0, args=""):
    time.sleep(delay*0.001)
    #begin = time.time()
    #print "delay %i start" % delay
    if rpc_type == "pyro":
        uri = "PYRO:test.RPC@%s:%i" % (host, port)
        remote = Pyro4.core.Proxy(uri)
    elif rpc_type == "rpyc":
        badhack = rpyc.connect(host, port)
        remote = badhack.root
    elif rpc_type == "grpc":
        # with rpc_test_pb2.early_adopter_create_SomeRemoteClass_stub(host, port) as stub:
        #     if read:
        #         response = stub.giveme(rpc_test_pb2.Empty(), _TIMEOUT_SECONDS)
        #         return len(response.message)
        #     else:
        #         stub.getit(rpc_test_pb2.GetitRequest(message=args), _TIMEOUT_SECONDS)
        #         return 0
        pass
    elif rpc_type == "web":
        remote = WebRemote(host, port)
    elif rpc_type == "zmq":
        remote = ZeroMQRemote(host, port)
    else:
        return 1

    if read:
        s = remote.giveme()
        res = len(s)
    else:
        remote.getit(args)
        res = 0
    #lat = time.time() - begin
    #print "delay %i finish, %i was working" % (delay, lat)
    return res


