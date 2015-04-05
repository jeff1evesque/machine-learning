#!/usr/bin/python

## @cache_interface.py
#  This file contains the required class to set, get, and delete various
#      memcached objects.
import memcache
from brain.memcached_settings import Memcached_Settings

## Class: Memcached, explicitly inherit 'new-style' class.
class Memcached(object):

    ## constructor:
    def __init__(self):
        self.host   = Memcached_Settings().get_host()
        self.port   = Memcached_Settings().get_port()
        self.server = memcache.Client([(self.host, self.port)])
 
    ## set: set value in memcached server.
    def set(self, key, value, expiry=900):
        self.server.set(key, value, expiry)
 
    ## get: retrieve value from memcached server.
    def get(self, key):
        return self.server.get(key)
 
    ## delete: delete value from memcached server.
    def delete(self, key):
        self.server.delete(key)
