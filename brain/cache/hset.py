#!/usr/bin/python

'''

This file caches, and uncaches supplied data using the redis hash cache.

'''

from brain.cache.query import Query


class Hset(object):
    '''

    This class provides an interface to cache, and uncache the redis hash
    data structure.  Specifically, necessary data components is passed into the
    corresponding class method.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''

        This constructor is responsible for defining class variables, as well
        as starting the redis client, in order to perform corresponding
        caching, and uncaching.

        '''

        # class variables
        self.list_error = []
        self.myRedis = Query()

        # start redis client
        try:
            self.myRedis.start_redis()
        except Exception as error:
            self.list_error.append(str(error))

    def cache(self, hash_name, key, value):
        '''

        This method caches the provided data into a redis hash cache.

        '''

        try:
            self.myRedis.hset(hash_name, key, value)
        except Exception as error:
            self.list_error.append(str(error))
            print self.list_error

    def uncache(self, hash_name, key):
        '''

        This method uncaches the provided key from a redis hash cache.

        '''

        try:
            return {'result': self.myRedis.hget(hash_name, key), 'error': None}
        except Exception as error:
            self.list_error.append(str(error))
            return {'result': None, 'error': self.list_error}
