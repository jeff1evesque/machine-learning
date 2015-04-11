#!/usr/bin/python

## @uncache_model.py
#  This file uncaches SVM models from the redis cache.
from brain.cache.redis_query import Redis_Query

## Class: Uncache_Model, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'views.py'.
class Uncache_Model(object):

    ## constructor
    def __init__(self):
        # class variables
        self.myRedis    = Redis_Query()
        self.list_error = []

        # start redis client
        try:
            self.myRedis.start_redis()
        except Exception, error:
            self.list_error.append(str(error))

    ## get_all_titles: query for the stored 'svm_models' in the redis hashed
    #                  cache.
    def get_all_titles(self, name):
        try:
            hkeys = self.myRedis.hkeys(name)
            return {'result': hkeys, 'error': None}
        except Exception, error:
            self.list_error.append(str(error))
            return {'result': None, 'error': self.list_error}
