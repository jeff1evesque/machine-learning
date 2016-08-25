#!/usr/bin/python

'''@sv

This file generates an sv prediction.

'''

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

    # get necessary model
    title = Cache_Hset().uncache(
        model + '_title',
        model_id
    )['result']
    clf = Cache_Model().uncache(
        model + '_model',
        model_id + '_' + title
    )

    # get encoded labels
    encoded_labels = Cache_Model().uncache(
        model + '_labels',
        model_id
    )

    # perform prediction, and return the result
    numeric_label = (clf.predict([predictors]))
    textual_label = list(encoded_labels.inverse_transform([numeric_label]))
    return {'result': textual_label[0][0], 'error': None}
