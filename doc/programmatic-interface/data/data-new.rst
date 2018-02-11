========
Data New
========

The ``data_new`` session, is an implementation that uploads new dataset(s), which can later be used
to generate successive models. There are two ways, for a ``data_new`` session to upload data, to the
``/load-data`` endpoint:

- dataset urls: ``json`` string, containing an array of ``dataset`` urls.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-data-new.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-data-new.json>`_

- file uploads: ``json`` string, containing an inline array of ``dataset`` values.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/file_upload/svm-data-new.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/file_upload/svr-data-new.json>`_

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
reviewed, in the ``/login`` `documentation <../authentication/login>`_.

The following properties define the above ``data`` attribute:

- ``session_name``: title for the corresponding ``data_new`` session

- ``collection``: collection of dataset documents, to be referenced during ``data_append``, ``model_generate``, and ``model_predict`` sessions

- ``dataset_type``: corresponds to one of the following types:

  - ``dataset_url``: indication that the supplied dataset will be url
    references
  - ``file_upload``: indication that the supplied dataset(s) will be
    defined as a json string within the ``dataset`` attribute

- ``session_type``: corresponds to one of the following session types:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``model_type``: the type of model to perform on:

  - ``svm``
  - ``svr``

- ``dataset``: the supplied dataset, contingent upon the ``dataset_type``
