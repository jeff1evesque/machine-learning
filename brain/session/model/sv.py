#!/usr/bin/python

'''

This file generates an sv model.

'''

from flask import current_app
from brain.database.dataset import Collection
from brain.cache.hset import Hset
from brain.cache.model import Model
from sklearn import svm, preprocessing
import json


def generate(model, kernel_type, collection, payload, list_error):
    '''

    This method generates an sv (i.e. svm, or svr) model using feature data,
    retrieved from the database. The generated model, is then stored within the
    NoSQL datastore.

    @grouped_features, a matrix of observations, where each nested vector,
        or python list, is a collection of features within the containing
        observation.
    @encoded_labels, observation labels (dependent variable labels),
        encoded into a unique integer representation.

    '''

    # local variables
    feature_labels = None
    label_encoder = preprocessing.LabelEncoder()
    list_model_type = current_app.config.get('MODEL_TYPE')
    collection_adjusted = collection.lower().replace(' ', '_')
    cursor = Collection()

    # get datasets
    datasets = cursor.query(
        collection_adjusted,
        'aggregate',
        payload
    )

    # restructure dataset into arrays
    observation_labels = []
    grouped_features = []
    raise ValueError('sv.py, datasets: ' + repr(list(datasets)))
    for dataset in datasets:
        for observation in dataset['dataset']:
            observation_labels.append(observation['dependent-variable'])

            indep_variables = observation['independent-variables']
            sorted_features = [v for k, v in sorted(indep_variables.items())]
            grouped_features.append(sorted_features)

            if not feature_labels:
                feature_labels = [k for k, v in sorted(indep_variables.items())]

    # generate svm model
    if model == list_model_type[0]:
        # convert observation labels to a unique integer representation
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(list(set(observation_labels)))
        encoded_labels = label_encoder.transform(observation_labels)

        # create model
        clf = svm.SVC(kernel=kernel_type, probability=True)

        # cache encoded labels
        Model(label_encoder).cache(model + '_labels', collection_adjusted)

        # fit model
        clf.fit(grouped_features, encoded_labels)

    # generate svr model
    elif model == list_model_type[1]:
        # create model
        clf = svm.SVR(kernel=kernel_type)

        # fit model
        clf.fit(grouped_features, observation_labels)

        # compute, and cache coefficient of determination
        r2 = clf.score(grouped_features, observation_labels)
        Hset().cache(
            model + '_r2',
            collection_adjusted,
            r2
        )

    # cache model, title
    Model(clf).cache(model + '_model', collection_adjusted)
    Hset().cache(
        model + '_collection',
        collection_adjusted,
        collection
    )

    # cache feature labels, with respect to given collection
    Hset().cache(
        model + '_feature_labels',
        collection,
        json.dumps(feature_labels)
    )

    # return error(s) if exists
    return {'error': list_error}
