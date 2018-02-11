===============
Data Attributes
===============

The programmatic-api, is intended to provide many of the functionalities, offered by the
web-interface. This is done by encoding equivalent attributes, into a json string, and
sent to its respective url endpoint, as an encapsulated ``POST`` request. Below, the
corresponding endpoints are briefly explained, and carefully linked, to further examples
of its implementation.


Main Session
============

- ``/load-data``: interfaces the following main sessions:

  - |data_new|_: store dataset(s) into the applications database
  - |data_append|_: append additional dataset(s), into an existing dataset entry in the database
  - |model_generate|_: generate a model, using an existing dataset entry from the database
  - |model_predict|_: generate a prediction, using an existing generated model

Result Arbiter
==============

- |/save-prediction|_: store a generated prediction, from a ``model_predict`` session.

- |/retrieve-prediction|_: retrieves the following saved prediction attributes:

  - result: pertains to all ``model_type``
  - classes: pertains only to the svm ``model_type``
  - decision function: pertains only to the svm ``model_type``
  - probabilities: pertains only to the svm ``model_type``
  - coefficient of determination: pertains only to the svr ``model_type``

- |/retrieve-prediction-titles|_: retrieves predictions saved titles, for either a specified
  ``model_type``, otherwise return all saved titles, for all ``model_type``.

.. |data_new| replace:: ``data_new``
.. _data_new: data/data-new
.. |data_append| replace:: ``data_append``
.. _data_append: data/data-append
.. |model_generate| replace:: ``model_generate``
.. _model_generate: model/model-generate
.. |model_predict| replace:: ``model_predict``
.. _model_predict: predict/model-predict.rst
.. |/save-prediction| replace:: ``/save-prediction``
.. _/save-prediction: result/save-prediction
.. |/retrieve-prediction| replace:: ``/retrieve-prediction``
.. _/retrieve-prediction: result/retrieve-prediction
.. |/retrieve-prediction-titles| replace:: ``/retrieve-prediction-titles``
.. _/retrieve-prediction-titles: result/retrieve-prediction-titles
