#!/usr/bin/python

## @model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'model_use.py'.
from brain.database.retrieve_feature import Retrieve_Feature
from sklearn import svm, preprocessing
import numpy

## Class: Model_Generate
#
#  Note: this class is invoked within 'load_data.py'
class Model_Generate():

    ## constructor:
    def __init__(self, svm_data):
        self.svm_data        = svm_data
        self.session_id      = self.svm_data['data']['settings']['svm_session_id']
        self.feature_request = Retrieve_Feature()
        self.list_error      = []

    ## generate_model: generate svm model
    #
    #  @X, observations
    #  @y, feature labels (independent variable labels)
    def generate_model(self):
        # local variables
        dataset       = self.feature_request.get_dataset(self.session_id)
        feature_count = self.feature_request.get_count(self.session_id)
        label_encoder = preprocessing.LabelEncoder()

        # get dataset
        if dataset['error']:
            print dataset['error']
            self.list_error.append(dataset['error'])
            dataset = None
        else:
            dataset = numpy.asarray(dataset['result'])

        # get feature count
        if feature_count['error']:
            print feature_count['error']
            self.list_error.append(feature_count['error'])
            feature_count = None
        else:
            feature_count = feature_count['result'][0][0]

        # check dataset integrity, build model
        if len(dataset) % feature_count == 0:
            features_list    = dataset[:, [2]]
            current_features = []
            grouped_features = []

            # group features into observation instances
            for index, feature in enumerate(features_list):
                if not (index+1) % feature_count == 0:
                    current_features.append(feature[0])
                else:
                    current_features.append(feature[0])
                    grouped_features.append(list_feature)
                    current_features = []

            y = label_encoder.transform(dataset[:, 0])

            # create svm model
            clf = svm.SVC()
            clf.fit(grouped_features, y)

    ## return_error: returns current error(s)
    def return_error(self):
        return self.list_error
