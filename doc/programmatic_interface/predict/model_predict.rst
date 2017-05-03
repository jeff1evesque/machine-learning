=============
Model Predict
=============

The ``model_predict`` session, is an implementation that performs a prediction, using
a previously generated model, from a ``model_generate``, session. There are two ways,
for a ``model_predict`` session to upload data, to the ``/load-data`` endpoint:

- dataset urls: ``json`` string, containing an array of ``dataset`` urls.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-model-predict.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-model-predict.json>`_

- file uploads: ``json`` string, containing an inline array of ``dataset`` values.

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/file_upload/svm-model-predict.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/file_upload/svr-model-predict.json>`_

**Note:** the content of each of the above files, can be substituted for
the ``data`` attribute.

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
