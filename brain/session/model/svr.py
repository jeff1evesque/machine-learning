#!/usr/bin/python

'''@svr

This file generates an svr model.

'''

from brain.database.retrieve_entity import Retrieve_Entity
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model
from sklearn import svr, preprocessing
from log.logger import Logger
import numpy
import json


def svr_model(kernel_type, session_id, feature_request, list_error):
    '''@svm_model

    This method generates an svr model using feature data, retrieved from
    the database. The generated model, is then stored within the NoSQL
    datastore.

    '''
