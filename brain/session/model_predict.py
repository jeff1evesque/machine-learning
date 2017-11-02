#!/usr/bin/python

'''

This file receives data (i.e. settings) required to query from the NoSQL
datastore, a previously stored SVM model, generated from 'model_generate.py'.
The determined SVM Model, is then used for analysis, based on the input data
provided during the current session, which generates an SVM prediction.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from flask import current_app
from brain.session.base import Base
from brain.session.predict import sv
from brain.session.predict import bag
from brain.database.model_type import ModelType


class ModelPredict(Base):
    '''

    This class provides an interface to generate a prediction, based on a
    specified model. Specifically, a prediction can be obtained by using the
    provided prediction feature input(s), and the stored corresponding model,
    within the NoSQL datastore.

    Note: inherit base methods from superclass 'Base'

    '''

    def __init__(self, prediction_input):
        '''

        This constructor is responsible for defining class variables, using the
        superclass 'Base' constructor, along with the constructor in this
        subclass.

        @super(), implement 'Base', and 'BaseData' superclass constructor
            within this child class constructor.

        @self.predictors, a list of arguments (floats) required to make a
            corresponding prediction, against the respective model.

        Note: the superclass constructor expects the same 'prediction_input'
              argument.

        '''

        super(ModelPredict, self).__init__(prediction_input)
        self.prediction_input = prediction_input
        self.prediction_settings = self.prediction_input['properties']
        self.collection = self.prediction_settings['collection']
        self.predictors = self.prediction_settings['prediction_input[]']

    def predict(self):
        '''

        This method generates a prediction with respect to the implemented
        model, using the provided prediction feature input(s), and the stored
        corresponding model, within the NoSQL datastore.

        '''

        list_model_type = current_app.config.get('MODEL_TYPE')
        # get model type
        model_type = ModelType().get_model_type(self.collection)['result']

        if model_type in [list_model_type[0], list_model_type[1]]:
            return sv.predict(model_type, self.collection, self.predictors)
        elif model_type in [list_model_type[2:10]]:
            return bag.predict(model_type, self.collection, self.predictors)
