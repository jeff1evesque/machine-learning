#!/usr/bin/python

## @cache_model.py
#  This file caches the supplied SVM model into the redis cache.
from brain.cache.redis_query import Redis_Query
from brain.converter.serialize_model import Serialize_Model
