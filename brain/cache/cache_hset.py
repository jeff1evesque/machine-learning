#!/usr/bin/python

## @cache_hset.py
#  This file caches, and uncaches supplied data using the redis hash
#      cache.
from brain.cache.redis_query import Redis_Query

## Class: Cache_Hset, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'cache_model.py'.
class Cache_Hset(object):

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

    ## uncache: uncache the provided key from a redis hash cache.
    def uncache(self, hash_name, key):
        try:
            return {'result': self.myRedis.hget(hash_name, key), 'error': None}
        except Exception, error:
            self.list_error.append(str(error))
            return {'result': None, 'error': self.list_error}
