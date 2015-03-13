#!/usr/bin/env python
import Pyro4
import rpyc

import rpc_test
# import rpc_test_pb2

def for_all_methods(decorator):
    def decorate(cls):
        for attr in cls.__bases__[0].__dict__:
            if callable(getattr(cls, attr)) and not attr.startswith('_'):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate

#@for_all_methods(Pyro4.oneway)
class SomeRemoteClass_Pyro(rpc_test.SomeRemoteClass):
    @Pyro4.oneway
    def getit(self, bigmsg):
        rpc_test.SomeRemoteClass.getit(self, bigmsg)


class SomeRemoteClass_Rpyc(rpc_test.SomeRemoteClass, rpyc.Service):
    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_giveme(self): # this is an exposed method
        return self.giveme()

    def exposed_getit(self, bigmsg): # this is an exposed method
        return self.getit(bigmsg)


# class SomeRemoteClass_gRpc(rpc_test_pb2.EarlyAdopterSomeRemoteClassServicer, rpc_test.SomeRemoteClass):
#     def getit(self, request, context):
#         rpc_test.SomeRemoteClass.getit(self, request.message)
#         return rpc_test_pb2.Empty()
#     def giveme(self, request, context):
#         a = rpc_test.SomeRemoteClass.giveme(self)
#         return rpc_test_pb2.GivemeReply(message=a)

class SomeRemoteClass_Web(rpc_test.SomeRemoteClass):
        def GET(self):
            return self.giveme()

