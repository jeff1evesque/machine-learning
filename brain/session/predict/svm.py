#!/usr/bin/python

'''@model_predict

This file receives data (i.e. settings) required to query from the NoSQL
datastore, a previously stored SVM model, generated from 'model_generate.py'.
The determined SVM Model, is then used for analysis, based on the input data
provided during the current session, which generates an SVM prediction.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model


def svm_prediction(model, kernel, model_id, predictors):
    '''@svm_prediction

    This method generates an svm prediction using the provided prediction
    feature input(s), and the stored corresponding model, within the NoSQL
    datastore.

    @prediction_input, a list of arguments (floats) required to make an SVM
        prediction, against the respective svm model.

    '''

    # get necessary model
    title = Cache_Hset().uncache(model+'_rbf_title', model_id)['result']
    clf = Cache_Model().uncache(
        model+'_rbf_model',
        self.model_id + '_' + title
    )

    # get encoded labels
    encoded_labels = Cache_Model().uncache(model+'_rbf_labels', model_id)

    # perform prediction, and return the result
    numeric_label = (clf.predict([predictors]))
    textual_label = list(encoded_labels.inverse_transform([numeric_label]))
    return {'result': textual_label[0][0], 'error': None}
