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
    def __init__(self, db_num=0):
        self.host   = Redis_Settings().get_host()
        self.port   = Redis_Settings().get_port()
        self.db_num = db_num
        self.server = redis.StrictRedis(host=self.host, port=self.port, db=db_num)

    ## set: set value into redis server.
    #
    #  Note: by default, redis keys are created without an associated time
    #        to live.  Therefore, the key will live until it is explicityl
    #        removed.
    def set(self, key, value):
        self.server.set(key, value)
 
    ## set: set value into redis server, with an expire time.
    def setex(self, key, value, time):
        self.server.set(key, value, time)

    ## set_expire: set an expire time (in seconds) for existing cached value.
    def set_expire(self, key, time):
        self.server.expire(key, time)

    ## get: retrieve value from redis server.
    def get(self, key):
        return self.server.get(key)
 
    ## delete: delete value from redis server.
    def delete(self, key):
        self.server.delete(key)
