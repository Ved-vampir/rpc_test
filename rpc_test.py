#!/usr/bin/env python

class SomeRemoteClass(object):
    def giveme(self):
        return "bla-"*10000

    def getit(self, bigmsg):
        print "get %i" % len(bigmsg)
