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
 
    ## setex: set value into redis server, with an expire time (in seconds).
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

    ## lset: set value to the index of the redis list.
    def lset(self, name, index, value):
        self.server.lset(name, index, value)

    ## lindex: return the element as defined redis list index.
    def lindex(self, name, index):
        return self.server.lindex(name, index)

    ## lrem: remove the first count occurences of elements equal to value
    #        within the redist list.
    def lrem(self, name, count, value)
        self.lrem(name, count, value)

    ## lpush: push values onto the beginning of a redis list.
    def lpush(self, name, *values):
        self.server.lpush(name, *values)

    ## rpush: push values onto the ending of a redis list.
    def rpush(self, name, *values):
        self.server.rpush(name, *values)

    ## lpop: remove, and return the first item of the redis list.
    def lpop(self, name):
        return self.server.lpop(name)

    ## rpop: remove, and return the last item of the redis list.
    def rpop(self, name):
        return self.server.rpop(name)

    ## ltrim: trim the redis list, removing all elements not within the
    #         slice bounds.
    def ltrim(self, name, start, end):
        self.server.ltrim(name, start, end)

    ## lrange: return a slice of the redis list between the slice bounds.
    def lrange(self, name, start, end):
        return self.server.lrange(name, start, end)
