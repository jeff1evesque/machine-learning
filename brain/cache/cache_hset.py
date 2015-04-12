#!/usr/bin/python

## @cache_hset.py
#  This file caches, and uncaches supplied data using the redis hash
#      cache.
from brain.cache.redis_query import Redis_Query

## Class: Cache_Hset, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'cache_model.py'.
class Cache_Model(object):

    ## constructor
    def __init__(self):
        # class variables
        self.list_error = []
        self.myRedis    = Redis_Query()

        # start redis client
        try:
            self.myRedis.start_redis()
        except Exception, error:
            self.list_error.append(str(error))

    ## cache: cache the provided data into a redis hash cache.
    def cache(self, hash_name, key, value):
        try:
            self.myRedis.hset(hash_name, key, value)
        except Exception, error:
            self.list_error.append(str(error))
            print self.list_error
