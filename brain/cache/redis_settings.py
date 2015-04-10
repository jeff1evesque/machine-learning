#!/usr/bin/python

## @redis_settings.py
#  This file contains the required class methods required to set, and
#      get the redis host, or memcache port.
from settings import HOST, PORT_REDIS

## Class: Redis_Settings, explicitly inherit 'new-style' class.
class Redis_Settings(object):

    ## constructor: define default redis host, and port.
    def __init__(self):
        self.host = HOST
        self.port = PORT_REDIS

    ## get_host: return the redis host.
    def get_host(self):
        return self.host

    ## get_port: return the redis port.
    def get_port(self):
        return self.port

    ## set_host: set the redis host.
    def set_host(self, host):
        self.host = host

    ## set_port: set the redis port.
    def set_port(self, port):
        self.port = port
