#!/usr/bin/python

## @model_predict.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'model_generate.py'. The
#      determined SVM Model is then used for analysis based on the input data
#      provided during the current session.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from brain.session.base import Base
from brain.validator.validate_settings import Validate_Settings
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model

## Class: Model_Predict, inherit base methods from superclass 'Base'
#
#  Note: this class is invoked within 'load_data.py'
class Model_Predict(Base):

    ## constructor: define class properties using the superclass 'Base'
    #               constructor, along with the constructor in this subclass.
    #
    #  @super(), implement 'Base', and 'Base_Data' superclass constructor within
    #      this child class constructor.
    #
    #  Note: the superclass constructor expects the same 'svm_data' argument.
    def __init__(self, svm_data):
        super(Model_Predict, self).__init__(svm_data)
        self.svm_data   = svm_data
        self.model_id   = self.svm_data['data']['settings']['svm_model_id']
        self.list_error = []

    ## svm_prediction: using supplied arguments, return an svm prediction from a
    #                  determined model.
    #
    #  @prediction_input, a list of arguments (floats) required to make an SVM
    #      prediction, against the respective svm model.
    def svm_prediction(self):
        # local variables
        prediction_input = self.svm_data['data']['settings']['prediction_input[]']

        # get necessary model
        svm_title = Cache_Hset().uncache('svm_title', self.model_id)['result']
        clf = Cache_Model().uncache('svm_model', self.model_id + '_' + svm_title)

        # get encoded labels
        encoded_labels = Cache_Model().uncache('svm_labels', self.model_id)

        # perform prediction, and return the result
        numeric_label = (clf.predict([prediction_input]))
        textual_label = list(encoded_labels.inverse_transform([numeric_label]))
        return textual_label
