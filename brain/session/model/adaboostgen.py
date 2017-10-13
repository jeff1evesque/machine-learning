import random
import numpy as np

from flask import current_app
from brain.database.dataset import Collection
from brain.cache.hset import Hset
from brain.cache.model import Model
import sklearn.ensemble
from sklearn import svm, preprocessing
import sklearn.ensemble
import json

def adaboosting(D, Y, C, k=50, be=None, learning=1.0, loss='linear'):
    # D is the dataset of features
    # Y is the classifications of each point in D
    # X is the points to be classified
    # be is the base estimator (which classifier type to ensemble?) Default
    #    is decision trees
    # k is the number of base estimators to use
    # features is how many to features to use for each estimator. 1.0
    #          means use them all.
    # samples is how many samples to draw for bagging purposes (see
    #         explanation of bagging)

    # set up the ensemble classifier
    if C:
        adaboostc = sklearn.ensemble.AdaBoostClassifier(base_estimator=be,
                                                     n_estimators=k,
                                                     learning_rate=learning)
    else:
        adaboostc = sklearn.ensemble.AdaBoostRegressor(base_estimator=be,
                                                    n_estimators=k,
                                                    learning_rate=learning,
                                                    loss=loss)

    # train the classifier
    return adaboostc.fit(D, Y)



# generic generate method for bagging
# regression is a boolean indicating whether this is a regression generator
def adaboostgen(model, regression, collection, payload, list_error, loss='linear', k=50, learning=1.0, be=None):
    sorted_labels = False
    label_encoder = preprocessing.LabelEncoder()
    collection_adjusted = collection.lower().replace(' ', '_')
    list_model_type = current_app.config.get('MODEL_TYPE')
    cursor = Collection()

    # datasets
    Ds = cursor.query(collection_adjusted, 'aggregate', payload)

    # the labels
    Y = []
    # the features
    F = []

    for D in Ds['result']:
        for o in D['dataset']:
            d = o['independent-variables']

            for f in d:
                if not regression:
                    Y.append(o['dependent-variable'])
                    sortedf = [v for k, v in sorted(f.items())]

                else:
                    Y.append(float(o['dependent-variable']))
                    sortedf = [float(v) for k, v in sorted(f.items())]

                F.append(sortedf)

                if not sorted_labels:
                    sorted_labels = [k for k, v in sorted(f.items())]

    #generate model

    if not regression:
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(Y)
        encoded_labels = label_encoder.transform(Y)

        # create and fit
        clf = adaboosting(F, Y, True, be=be, learning=learning, k=k)

        Model(label_encoder).cache(model + '_labels', collection_adjusted)

    else:
        # create and fit
        clf = adaboosting(F, Y, False, be=be, learning=learning, k=k, loss=loss)

        r2 = clf.score(F, Y)

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

