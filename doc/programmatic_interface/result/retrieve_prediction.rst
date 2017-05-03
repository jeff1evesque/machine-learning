===================
Retrieve Prediction
===================

The ``retrieve_prediction`` session, is an implementation that retrieves a specified saved
prediction, from the applications database, via the ``/retrieve-prediction`` endpoint:

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/results/retrieve-prediction.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/results/retrieve-prediction.json>`_

**Note:** the content of each of the above examples, can be substituted for
the ``data`` attribute, in a given ``POST`` request:

.. code:: python

    import requests

    endpoint_url = 'http://localhost:8080/[END-POINT]'
    headers = {'Content-Type': 'application/json'}

    requests.post(endpoint_url, headers=headers, data=json_string_here)

The following properties define the above ``data`` attribute:

- ``id_result``: corresponds to the id of the desired model.

- ``model_type``: corresponds to the desired model type:

  - ``all``: pertains to all stored model types
  - ``svm``: pertains only to the support vector machine model type
  - ``svr``: pertains only to the suppport vector regression model type
