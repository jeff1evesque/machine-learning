===============
Save Prediction
===============

The ``save_prediction`` session, is an implementation that saves a supplied prediction
result, into the applications database, via the ``/save-prediction`` endpoint:

- `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/results/save-prediction.json>`_
- `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/results/save-prediction.json>`_

**Note:** the content of each of the above examples, can be substituted for
the ``data`` attribute, in a given ``POST`` request:

.. code:: python

    import requests

    endpoint = 'https://localhost:9090/save-prediction'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    requests.post(endpoint, headers=headers, data=json_string_here)

**Note:** more information, regarding how to obtain a valid ``token``, can be further
reviewed, in the ``/login`` `documentation <https://github.com/jeff1evesque/machine-learning/tree/master/doc/programmatic_interface/authentication/login.rst>`_.

The following properties define the above ``data`` attribute:

- ``status``: provides the application utilizing this programmatic-api, an additional
  layer to perform conditional sanity checks, before storing the corresponding results:

  - ``valid``: indication to proceed storing result into the database

- ``model_type``: corresponds to the desired model type:

  - ``svm``: pertains only to the support vector machine model type
  - ``svr``: pertains only to the suppport vector regression model type

- ``title``: desired name to assign the proposed prediction result.

- ``data``:

  - ``result``: the computed result of the prediction
  - ``classes``: applies only to the svm prediction
  - ``probability``: applies only to the svm prediction
  - ``decision_function``: applies only to the svm prediction
  - ``r2``: applies only to the svr prediction
