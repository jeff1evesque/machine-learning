#!/usr/bin/python

'''@svr

This file generates an svr model.

'''

from brain.database.retrieve_entity import Retrieve_Entity
from brain.cache.cache_hset import Cache_Hset
from brain.cache.cache_model import Cache_Model
from sklearn import svm, preprocessing
from log.logger import Logger
import numpy
import json


def svr_model(kernel_type, session_id, feature_request, list_error):
    '''@svm_model

    This method generates an svr model using feature data, retrieved from
    the database. The generated model, is then stored within the NoSQL
    datastore.

    '''

    # local variables
    dataset = feature_request.get_dataset(session_id)
    get_feature_count = feature_request.get_count(session_id)
    label_encoder = preprocessing.LabelEncoder()
    logger = Logger(__name__, 'error', 'error')

    # get dataset
    if dataset['error']:
        logger.log(dataset['error'])
        list_error.append(dataset['error'])
        dataset = None
    else:
        dataset = numpy.asarray(dataset['result'])

    # check dataset integrity, build model
    if len(dataset) % feature_count == 0:
        features_list = dataset[:, [[0], [2], [1]]]
        current_features = []
        grouped_features = []
        observation_labels = []
        feature_labels = []

        # group features into observation instances, record labels
        for index, feature in enumerate(features_list):
            if not (index+1) % feature_count == 0:
                # observation labels
                current_features.append(feature[1][0])

                # general feature labels in every observation
                if not len(feature_labels) == feature_count:
                    feature_labels.append(feature[2][0])
            else:
                # general feature labels in every observation
                if not len(feature_labels) == feature_count:
                    feature_labels.append(feature[2][0])

                current_features.append(feature[1][0])
                grouped_features.append(current_features)
                observation_labels.append(feature[0][0])
                current_features = []

        # convert observation labels to a unique integer representation
        label_encoder = preprocessing.LabelEncoder()
        label_encoder.fit(dataset[:, 0])
        encoded_labels = label_encoder.transform(observation_labels)

        # create svr model
        clf = svm.SVR(kernel=kernel_type)
        clf.fit(grouped_features, encoded_labels)

        # get svr title, and cache (model, encoded labels, title)
        entity = Retrieve_Entity()
        title = entity.get_title(session_id)['result'][0][0]
        Cache_Model(clf).cache(
            'svr_model',
            str(session_id) + '_' + title
        )
        Cache_Model(label_encoder).cache('svr_labels', session_id)
        Cache_Hset().cache('svr_title', session_id, title)

        # cache svr feature labels, with respect to given session id
        Cache_Hset().cache(
            'svr_feature_labels',
            'svr_feature_labels',
            str(session_id),
            json.dumps(feature_labels)
        )

        # return error(s) if exists
        return {'error': list_error}
