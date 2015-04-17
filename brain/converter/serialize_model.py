#!/usr/bin/python

## @serialize_model.py
#  This file serializes, and deserializes an SVM object in memory.
from six.moves import cPickle as pickle
from sklearn import svm, preprocessing

## Class: Serialize_Model, explicitly inherit 'new-style class.
#
#  Note: this class is invoked within 'cache_model.py'.
class Serialize_Model(object):

    ## constructor
    def __init__(self, model):
        self.model = model
        self.acceptable = [svm.classes.SVC, preprocessing.label.LabelEncoder]

    ## serialize: serializes the provided object.
    def serialize(self):
        if type(self.model) in self.acceptable:
            return pickle.dumps(self.model)

    ## deserialize: deserializes the provided object.
    def deserialize(self):
        return pickle.loads(self.model)
