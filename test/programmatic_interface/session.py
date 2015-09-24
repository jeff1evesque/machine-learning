"""@session

This module will test the following sessions:

  - data_new: stores supplied dataset into a SQL database.
  - data_append: appends supplied dataset to an already stored
                 dataset in an SQL database.
  - model_generate: generate an model by selecting a particular
                    range of dataset (session), and store it
                    into a NoSQL cache.
  - model_predict: generate a prediction by selecting a particular
                   cached model from the NoSQL cache.

  Note: this module requires the installation of 'pytest':

      - pip install pytest

"""
import requests
import json
import os.path.join

# import sample dataset
with open(os.path.join('..', '..', 'interface', 'static', 'data', 'json', 'sample-1.json')) as json_file:
    json_dataset = json.load(json_file)

def data_new(data):
    """@data_new

    This method tests the 'data_new' session
    """

    r = requests.post('localhost:5000/load-data/', data=json_dataset)
