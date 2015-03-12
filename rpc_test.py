#!/usr/bin/env python

import os

class SomeRemoteClass(object):
    def giveme(self):
        return os.urandom(40000)

    def getit(self, bigmsg):
        print "get %i" % len(bigmsg)
