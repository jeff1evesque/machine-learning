#!/usr/bin/python

'''@svm

This file generates an svm prediction.

'''

from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model


def svm_prediction(model, kernel, model_id, predictors):
    '''@svm_prediction

    This method generates an svm prediction using the provided prediction
    feature input(s), and the stored corresponding model, within the NoSQL
    datastore.

    @predictors, a list of arguments (floats) required to make an SVM
        prediction, against the respective svm model.

    '''

    # get necessary model
    title = Cache_Hset().uncache(model + '_' + kernel + '_title', model_id)['result']
    clf = Cache_Model().uncache(
        model + '_' + kernel + '_model',
        model_id + '_' + title
    )

    # get encoded labels
    encoded_labels = Cache_Model().uncache(model + '_' + kernel + '_rbf_labels', model_id)

    # perform prediction, and return the result
    numeric_label = (clf.predict([predictors]))
    textual_label = list(encoded_labels.inverse_transform([numeric_label]))
    return {'result': textual_label[0][0], 'error': None}
