#!/usr/bin/python

## @memcached_settings.py
#  This file contains the required class methods required to set, and
#      get the memcache host, or memcache port.

## Class: Memcached_Settings, explicitly inherit 'new-style' class.
class Memcached_Settings(object):

    ## constructor: define default memcached host, and port.
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000

    ## get_host: return the memcached host.
    def get_host(self):
        return self.host

    ## get_port: return the memcached port.
    def get_port(self):
        return self.port

    ## set_host: set the memcached host.
    def set_host(self, host):
        self.host = host

    ## set_port: set the memcached port.
    def set_port(self, port):
        self.port = port
