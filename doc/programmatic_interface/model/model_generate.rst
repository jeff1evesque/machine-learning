==============
Model Generate
==============

The ``model_generate`` session, is an implementation that generates a desired model,
using previously uploaded dataset(s), via either the ``data_new``, or the ``data_append``
session. The required attributes, for the corresponding session, is sent to the
``/load-data`` endpoint, which is demonstrated as follows:

- `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-model-generate.json>`_
- `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-model-generate.json>`_
- `bagc example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/bagc/dataset_url/bagc-model-generate.json>`_

**Note:** the content of each of the above examples, can be substituted for
the ``data`` attribute, in a given ``POST`` request:

.. code:: python

    import requests

    endpoint_url = 'https://localhost:8080/load-data'
    headers = {'Content-Type': 'application/json'}

    requests.post(endpoint_url, headers=headers, data=json_string_here)

The following properties define the above ``data`` attribute:

- ``collection``: collection of dataset documents, used to generate a model

- ``session_type``: corresponds to one of the following session types:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``model_type``: the type of model to perform on:

  - ``svm``
  - ``svr``
  - ``bagc``

- ``sv_kernel_type``: the type of kernel to apply to the support vector ``model_type``:

  -  ``linear``
  -  ``polynomial``
  -  ``rbf``
  -  ``sigmoid``
