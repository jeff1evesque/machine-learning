#!/usr/bin/python

from flask import current_app
from brain.database.dataset import Collection
from brain.cache.hset import Hset
from brain.cache.model import Model
from sklearn import preprocessing
import sklearn.ensemble
import json


def bagging(
    dataset,
    classes,
    model,
    k=10,
    be=None,
    features=1.0,
    samples=1.0
):
    '''

    This function trains the provided dataset, with the following properties:

    @dataset, the dataset of features
    @labels, the classifications of each point in D
    @be, the base estimator (which classifier type to ensemble?)
        - default is decision trees
    @k, the number of base estimators to use
    @features, how many to features to use for each estimator. 1.0 means use
        them all.
    @samples, how many samples to draw for bagging purposes

    '''

    # local variables
    list_model_type = current_app.config.get('MODEL_TYPE')

    # set up the ensembler
    if model == list_model_type[3]:
        bagger = sklearn.ensemble.BaggingClassifier(
            base_estimator=be,
            n_estimators=k,
            max_samples=samples,
            max_features=features,
            verbose=0
        )
    elif model == list_model_type[4]:
        bagger = sklearn.ensemble.BaggingRegressor(
            base_estimator=be,
            n_estimators=k,
            max_samples=samples,
            max_features=features,
            verbose=0
        )

    # train bagger
    return bagger.fit(dataset, labels)


def baggen(
    model,
    collection,
    payload,
    list_error,
    feat=1.0,
    samples=1.0,
    be=None,
    k=10
):
    '''

    This function generates the corresponding ensemble bagger.

    '''

    # local variables
    labels = []
    features = []
    cursor = Collection()
    sorted_labels = False
    label_encoder = preprocessing.LabelEncoder()
    list_model_type = current_app.config.get('MODEL_TYPE')
    collection_adjusted = collection.lower().replace(' ', '_')
    datasets = cursor.query(collection_adjusted, 'aggregate', payload)

    for D in datasets['result']:
        for o in D['dataset']:
            d = o['independent-variables']

            for f in d:
                if regression:
                    labels.append(float(o['dependent-variable']))
                    sortedf = [float(v) for k, v in sorted(f.items())]
                else:
                    labels.append(o['dependent-variable'])
                    sortedf = [v for k, v in sorted(f.items())]

                features.append(sortedf)

                if not sorted_labels:
                    sorted_labels = [k for k, v in sorted(f.items())]

    # generate model
    if model == list_model_type[3]:
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(labels)
        encoded_labels = label_encoder.transform(labels)

        # create and fit
        clf = bagging(
            features,
            encoded_labels,
            model,
            be=be,
            features=feat,
            samples=samples,
            k=k
        )

        Model(label_encoder).cache(model + '_labels', collection_adjusted)

    else if model == list_model_type[4]:
        # create and fit
        clf = bagging(
            features,
            labels,
            model,
            be=be,
            features=feat,
            samples=samples,
            k=k
        )

        r2 = clf.score(F, labels)

        Hset().cache(
            model + '_r2',
            collection_adjusted,
            r2
        )

    Model(clf).cache(model + '_model', collection_adjusted)

    Hset().cache(
        model + '_feature_labels',
        collection,
        json.dumps(sorted_labels)
    )

    return {'error': list_error}
