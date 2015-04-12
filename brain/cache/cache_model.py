#!/usr/bin/python

## @cache_model.py
#  This file caches the supplied SVM model into the redis cache.
from brain.cache.redis_query import Redis_Query
from brain.converter.serialize_model import Serialize_Model

## Class: Cache_Model, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'model_generate.py'.
class Cache_Model(object):

    ## constructor
    def __init__(self, model=None):
        # class variables
        self.model      = model
        self.list_error = []
        self.myRedis    = Redis_Query()

        # start redis client
        try:
            self.myRedis.start_redis()
        except Exception, error:
            self.list_error.append(str(error))

    ## cache: serialize the provided svm model, then store into the
    #         redis hash cache.
    def cache(self, hash_name, key):
        try:
            serialized = Serialize_Model(self.model).serialize()
            self.myRedis.hset(hash_name, key, serialized)
        except Exception, error:
            self.list_error.append(str(error))
            print self.list_error
