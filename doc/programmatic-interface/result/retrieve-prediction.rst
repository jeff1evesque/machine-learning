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

    endpoint = 'https://localhost:9090/retrieve-prediction'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    requests.post(endpoint, headers=headers, data=json_string_here)

**Note:** more information, regarding how to obtain a valid ``token``, can be further
reviewed, in the ``/login`` `documentation <../authentication/login>`_.

The following properties define the above ``data`` attribute:

- ``id_result``: corresponds to the id of the desired model.
