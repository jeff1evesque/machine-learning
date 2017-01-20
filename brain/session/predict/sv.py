#!/usr/bin/python

'''

This file generates an sv prediction, and can return associated confidence
levels, associated with corresponding predictions.

'''

from flask import current_app
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model


def sv_prediction(model, model_id, predictors):
    '''

    This method generates an sv (i.e. svm, or svr) prediction using the
    provided prediction feature input(s), and the stored corresponding model,
    within the NoSQL datastore.

    Additionally, the following is returned for SVM predictions:

        - array of probability a given point (predictors) is one of the
          defined set of classifiers.
        - array of sum distances a given point (predictors) is to the set
          of associated hyperplanes.

    However, the following is returned for SVR predictions:

        - coefficient of determination (r^2).


    @clf, decoded model, containing several methods (i.e. predict)

    @predictors, a list of arguments (floats) required to make an SVM
        prediction, against the respective svm model.

    '''

    # local variables
    probability = None
    decision_function = None
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

    # perform prediction, and return the result
    prediction = (clf.predict([predictors]))

    # case 1: return svm prediction, and confidence level
    if model == list_model_type[0]:
        encoded_labels = Cache_Model().uncache(
            model + '_labels',
            model_id
        )

        textual_label = encoded_labels.inverse_transform([prediction])
        probability = clf.predict_proba(predictors)
        decision_function = clf.decision_function(predictors)
        classes = [encoded_labels.inverse_transform(x) for x in clf.classes_]

        return {
            'result': textual_label[0][0],
            'model': model,
            'confidence': {
                'classes': list(classes),
                'probability': list(probability[0]),
                'decision_function': list(decision_function[0])
            },
            'error': None
        }

    # case 2: return svr prediction, and confidence level
    elif model == list_model_type[1]:
        r2 = Cache_Hset().uncache(
            model + '_r2',
            model_id
        )['result']

        return {
            'result': str(prediction[0]),
            'model': model,
            'confidence': {
                'score': r2
            },
            'error': None
        }
