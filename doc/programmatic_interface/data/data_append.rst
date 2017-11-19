===========
Data Append
===========

The ``data_append`` session, is an implementation that appends additional dataset(s), to
a previous implemented ``data_new`` session. Like the ``data_new`` session, there are two
ways to upload data, to the ``/load-data`` endpoint:

- dataset urls: ``json`` string, containing an array of ``dataset`` urls.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-data-append.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-data-append.json>`_

- file uploads: ``json`` string, containing an inline array of ``dataset`` values.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/file_upload/svm-data-append.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/file_upload/svr-data-append.json>`_

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
reviewed, in the ``/login`` `documentation <https://github.com/jeff1evesque/machine-learning/tree/master/doc/programmatic_interface/authentication/login.rst>`_.

The following properties define the above ``data`` attribute:

- ``collection``: collection of dataset documents, used as a reference to add additional dataset documents into

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

- ``session_id``: corresponds to the id associated with the original ``data_new``
  uploaded dataset(s), being appended to.

- ``dataset``: the supplied dataset, contingent upon the ``dataset_type``
