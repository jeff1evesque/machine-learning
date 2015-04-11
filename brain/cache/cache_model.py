#!/usr/bin/python

## @cache_model.py
#  This file caches the supplied SVM model into the redis cache.
from brain.cache.redis_query import Redis_Query
from brain.converter.serialize_model import Serialize_Model

## Class: Cache_Model, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'model_generate.py', and
#        'model_use.py'
class Cache_Model(object):

    ## constructor
    def __init__(self, model):
        # define class variables
        self.model   = model
        self.myRedis = Redis_Query()

        # start redis client
        self.myRedis.start_redis()

    ## cache: serialize the provided svm model, then store into the
    #         redis hash cache.
    def cache(self, hash_name, key):
        serialized = Serialize_Model(self.model).serialize()
        self.myRedis.hset(hash_name, key, serialized)
