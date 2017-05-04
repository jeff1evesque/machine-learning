=============
Model Predict
=============

The ``model_predict`` session, is an implementation that performs a prediction, using a
previously generated model, from a ``model_generate`` session. The required attributes,
needed for the corresponding session, is sent to the ``/load-data`` endpoint as follows:

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-model-predict.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-model-predict.json>`_

**Note:** the content of each of the above examples, can be substituted for
the ``data`` attribute, in a given ``POST`` request:

.. code:: python

    import requests

    endpoint_url = 'http://localhost:8080/[END-POINT]'
    headers = {'Content-Type': 'application/json'}

    requests.post(endpoint_url, headers=headers, data=json_string_here)

The following properties define the above ``data`` attributes:

- ``session_type``: corresponds to one of the following session types:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``model_id``: corresponds to the id associated with a previous ``model_generate``
  session.

- ``prediction_input[]``: an array of prediction input, supplied to the previously
   generated model to compute a prediction.
