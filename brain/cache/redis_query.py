#!/usr/bin/python

## @redis_query.py
#  This file contains the required class to set, get, and delete various
#      redis-cached objects.
import redis
from brain.cache.redis_settings import Redis_Settings

## Class: Memcached, explicitly inherit 'new-style' class.
class Memcached(object):

    ## constructor: defines class variables.
    #
    # @db, the redis database number to store jobs into (there are 0-15).
    def __init__(self):
        self.host   = Redis_Settings().get_host()
        self.port   = Redis_Settings().get_port()
        self.server = redis.StrictRedis(host=self.host, port=self.port, db=0)
 
    ## set: set value in memcached server.
    def set(self, key, value, expiry=900):
        self.server.set(key, value, expiry)
 
    ## get: retrieve value from memcached server.
    def get(self, key):
        return self.server.get(key)
 
    ## delete: delete value from memcached server.
    def delete(self, key):
        self.server.delete(key)
