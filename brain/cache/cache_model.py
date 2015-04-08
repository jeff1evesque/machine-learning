#!/usr/bin/python

## @cache_model.py
#  This file caches the supplied SVM model into the redis cache.
from brain.cache.redis_query import Redis_Query
from brain.converter.serialize_model import Serialize_Model

    ## Class: Cache_Model, explicitly inherit 'new-style class.
    #
    #  Note: this class is invoked within 'model_generate.py', and
    class Cache_Model(object):

        ## constructor
        def __init__(self, model):
            self.model = model

        ## cache: serialize the provided svm model, then store into the
        #         redis cache.
        def cache(self, key):
            serialized = Serialize_Model().serialize(self.model)
            myRedis    = Redis_Query()

            myRedis.start_redis()
            myRedis.hset('svm_models', key, serialized)
