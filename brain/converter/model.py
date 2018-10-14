#!/usr/bin/python

'''

This file serializes, and deserializes an SVM object

'''

from six.moves import cPickle as pickle
from sklearn import svm, preprocessing


class Model:
    '''

    This class provides an interface to serialize, and deserialize an SVM
    object.

    '''

    def __init__(self, model):
        '''

        This constructor saves an model, and defines the acceptable set of
        class instance type, the provided model is allowed to be.

        '''

        self.model = model
        self.acceptable = [
            svm.classes.SVC,
            svm.classes.SVR,
            preprocessing.label.LabelEncoder
        ]

    def serialize(self):
        '''

        This method serializes the provide model.

        '''

        if type(self.model) in self.acceptable:
            return pickle.dumps(self.model)

    def deserialize(self):
        '''

        This method deserializes the provided object.

        '''

        return pickle.loads(self.model)
