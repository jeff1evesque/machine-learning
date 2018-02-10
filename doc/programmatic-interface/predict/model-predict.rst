=============
Model Predict
=============

The ``model_predict`` session, is an implementation that performs a prediction, using a
previously generated model, from a ``model_generate`` session. The required attributes,
for the corresponding session, is sent to the ``/load-data`` endpoint, which is
demonstrated as follows:

- `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-model-predict.json>`_
- `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-model-predict.json>`_

**Note:** the content of each of the above examples, can be substituted for
the ``data`` attribute, in a given ``POST`` request:

.. code:: python

    import requests

    endpoint = 'https://localhost:9090/load-data'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    requests.post(endpoint, headers=headers, data=json_string_here)

**Note:** more information, regarding how to obtain a valid ``token``, can be further
reviewed, in the ``/login`` `documentation </latest/html/programmatic-interface/authentication/login>`_.

The following properties define the above ``data`` attribute:

- ``collection``: collection of dataset documents, used to generate a model, via the `model_generate` session,
  which is also used to name the corresponding model

- ``session_type``: corresponds to one of the following session types:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``model_id``: corresponds to the id associated with a previous ``model_generate``
  session.

- ``prediction_input[]``: an array of prediction input, supplied to the previously
  generated model to compute a prediction.
