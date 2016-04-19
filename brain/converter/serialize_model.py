#!/usr/bin/python

'''@serialize_model

This file serializes, and deserializes an SVM object

'''

from six.moves import cPickle as pickle
from sklearn import svm, preprocessing


class Serialize_Model(object):
    '''@Serialize_Model

    This class provides an interface to serialize, and deserialize an SVM
    object.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, model):
        '''@__init__

        This constructor saves an model, and defines the acceptable set of
        class instance type, the provided model is allowed to be.

        '''

        self.model = model
        self.acceptable = [svm.classes.SVC, preprocessing.label.LabelEncoder]

    def serialize(self):
        '''@serialize

        This method serializes the provide model.

        '''

        if type(self.model) in self.acceptable:
            return pickle.dumps(self.model)

    def deserialize(self):
        '''@deserialize

        This method deserializes the provided object.

        '''

        return pickle.loads(self.model)
