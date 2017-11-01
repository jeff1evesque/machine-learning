#!/usr/bin/python

from brain.database.dataset import Collection
from brain.cache.hset import Hset
from brain.cache.model import Model
from sklearn import preprocessing
import sklearn.ensemble
import json


def adaboosting(
    dataset,
    labels,
    model,
    k=50,
    be=None,
    learning=1.0,
    loss='linear'
):
    '''

    This function trains the provided dataset, with the following properties:

    @dataset, the dataset of features
    @labels, the classifications of each point in D
    @be, the base estimator (which classifier type to ensemble?)
        - default is decision trees
    @k, the number of base estimators to use
    @learning, shrinks the contribution of each estimator
    @loss, only used for regressors, the function to update the weights after
        each boosting operation

    '''

    # local variables
    classifiers = ['adaboostknnr', 'adaboostrfr', 'adaboostsvr', 'adaboostr']
    regressors = ['adaboostknnc', 'adaboostrfc', 'adaboostsvc', 'adaboostc']

    # set up the ensembler
    if model in classifiers:
        booster = sklearn.ensemble.AdaBoostClassifier(
            base_estimator=be,
            n_estimators=k,
            learning_rate=learning
        )
    elif model in regressors:
        booster = sklearn.ensemble.AdaBoostRegressor(
            base_estimator=be,
            n_estimators=k,
            learning_rate=learning,
            loss=loss
        )

    # train booster
    return booster.fit(dataset, labels)


def adaboostgen(
    model,
    collection,
    payload,
    list_error,
    learning=1.0,
    loss='linear',
    be=None,
    bnum=50
):
    '''

    This function generates the corresponding ensemble booster.

    '''

    # local variables
    labels = []
    features = []
    cursor = Collection()
    sorted_labels = False
    label_encoder = preprocessing.LabelEncoder()
    collection_adjusted = collection.lower().replace(' ', '_')
    datasets = cursor.query(collection_adjusted, 'aggregate', payload)
    classifiers = ['adaboostknnr', 'adaboostrfr', 'adaboostsvr', 'adaboostr']
    regressors = ['adaboostknnc', 'adaboostrfc', 'adaboostsvc', 'adaboostc']

    for D in datasets['result']:
        for o in D['dataset']:
            d = o['independent-variables']

            for f in d:
                if model in regressors:
                    labels.append(float(o['dependent-variable']))
                    sortedf = [float(v) for k, v in sorted(f.items())]
                elif model in classifiers:
                    labels.append(o['dependent-variable'])
                    sortedf = [v for k, v in sorted(f.items())]

                features.append(sortedf)

                if not sorted_labels:
                    sorted_labels = [k for k, v in sorted(f.items())]

    # generate model
    if model in classifiers:
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(labels)
        encoded_labels = label_encoder.transform(labels)

        # create and fit
        clf = adaboosting(
            features,
            encoded_labels,
            model,
            be=be,
            learning=learning,
            k=bnum
        )

        Model(label_encoder).cache(model + '_labels', collection_adjusted)

    elif model in regressors:
        # create and fit
        clf = adaboosting(
            features,
            labels,
            model,
            be=be,
            learning=learning,
            loss=loss,
            k=bnum
        )

        r2 = clf.score(features, labels)

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
