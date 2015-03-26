#!/usr/bin/python

## @model_generate.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and generates an SVM model, respectively. The new SVM model, is stored
#      into respective database table(s), which later can be retrieved within
#      'model_use.py'.

## Class: Model_Generate
#
#  Note: this class is invoked within 'load_data.py'
class Model_Generate():

    ## constructor:
    def __init__(self, svm_data):
        self.svm_data = svm_data

    ## save_svm_info: save the number of features that can be expected in a given
    #                 observation with respect to 'id_entity'.
    def save_svm_info(self):
        for data in self.dataset:
            for dataset in data['svm_dataset']:
                db_save = Save_Size({'id_entity': data['id_entity'], 'count_features': data['count_features']})

                # save dataset element, append error(s)
                db_return = db_save.save()
                if db_return['error']: self.response_error.append(db_return['error'])
