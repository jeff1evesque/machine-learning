#!/usr/bin/python

'''

This file caches, and uncaches the supplied model into a redis hash cache.

'''

from brain.cache.query import Query
from brain.converter.model import Model as Converter


class Model(object):
    '''

    This class provides an interface to cache, and uncache the redis hash
    data structure.  Specifically, necessary data components is passed into the
    corresponding class method, which allow computed model(s) to be stored into
    a NoSQL datastore.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, model=None):
        '''

        This constructor is responsible for defining class variables, as well
        as starting the redis client, in order to perform corresponding
        caching, and uncaching.

        '''

        # class variables
        self.model = model
        self.list_error = []
        self.myRedis = Query()

        # start redis client
        try:
            self.myRedis.start_redis()
        except Exception as error:
            self.list_error.append(str(error))

    def cache(self, hash_name, key):
        '''

        This method serializes, then caches the provided model into a redis
        hash cache.

        '''

        try:
            serialized = Converter(self.model).serialize()
            self.myRedis.hset(hash_name, key, serialized)
        except Exception as error:
            self.list_error.append(str(error))
            print self.list_error

    def uncache(self, hash_name, key):
        '''

        This method unserializes, then uncaches the desired model, using
        the provided key from the redis hash cache.

        '''

        uncached = self.myRedis.hget(hash_name, key)
        return Converter(uncached).deserialize()

    def get_all_titles(self, name):
        '''

        This method returns a list of all models, with respect to the provided
        redis key, in the form of the corresponding model_type (i.e svm_model).

        Note: each model will be named, with the supplied 'session_name' value,
              provided during the corresponding 'data_new' session.

        '''

        try:
            # get model(s)
            hkeys = self.myRedis.hkeys(name)
            list_title = []

            for i in range(len(hkeys)):
                list_title.append({'collection': hkeys[i]})

            # return result
            if list_title:
                return {'result': list_title, 'error': None}
            else:
                return {
                    'result': None,
                    'error': 'no previous model found in cache'
                }

        except Exception as error:
            self.list_error.append(str(error))
            return {'result': None, 'error': self.list_error}
