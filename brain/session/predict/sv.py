#!/usr/bin/python

'''@sv

This file generates an sv prediction.

'''

from flask import current_app
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model


def sv_prediction(model, model_id, predictors):
    '''@sv_prediction

    This method generates an sv (i.e. svm, or svr) prediction using the
    provided prediction feature input(s), and the stored corresponding model,
    within the NoSQL datastore.

    @clf, decoded model, containing several methods (i.e. predict)

    @predictors, a list of arguments (floats) required to make an SVM
        prediction, against the respective svm model.

    '''

    # local variables
    list_model_type = current_app.config.get('MODEL_TYPE')

    # get necessary model
    title = Cache_Hset().uncache(
        model + '_title',
        model_id
    )['result']
    clf = Cache_Model().uncache(
        model + '_model',
        model_id + '_' + title
    )

    # svm model: get encoded labels
    if model == list_model_type[0]:
        encoded_labels = Cache_Model().uncache(
            model + '_labels',
            model_id
        )

    # perform prediction
    numeric_label = (clf.predict([predictors]))

    # result: svm model
    if model == list_model_type[0]:
        textual_label = list(encoded_labels.inverse_transform([numeric_label]))
        return {'result': textual_label[0][0], 'error': None}

    # result: svr model
    elif model == list_model_type[1]:
        return {'result': str(numeric_label[0]), 'error': None}
