#!/usr/bin/python

## @uncache_model.py
#  This file uncaches SVM models from the redis cache.
from brain.cache.redis_query import Redis_Query

## Class: Uncache_Model, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'views.py'.
class Uncache_Model(object):

