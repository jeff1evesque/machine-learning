===============
Data Attributes
===============

The programmatic-api is intended to provide the same functionality as the web-interface,
with the exception that corresponding commands, are contained within various attributes,
encapsulated into a ``POST`` request, and sent to its respective url endpoint.

Main Session:
=============

- ``/load-data``: which supports the following sessions:

  - |data_new|_: store dataset(s) into the applications database
  - |data_append|_: append additional dataset(s), into an existing dataset entry in the database
  - |model_generate|_: generate a model, using an existing dataset entry from the database
  - |model_predict|_: generate a prediction, using an existing generated model

Result Arbiter:
===============

- ``/save-prediction``: store a generated prediction, from a ``model_predict`` session.

- ``/retrieve-prediction``: retrieves the following saved prediction attributes:

  - result: pertains to all ``model_type``
  - classes: pertains only to svm ``model_type``
  - decision function: pertains only to svm ``model_type``
  - probabilities: pertains only to svm ``model_type``
  - coefficient of determination: pertains only to svr ``model_type``

- ``/retrieve-prediction-titles``: retrieves predictions saved titles, for either a specified
  ``model_type``, otherwise return all saved titles, for all ``model_type``.

.. |data_new| replace:: ``data_new``
.. _data_new: https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic-api/data/data_new.rst
.. |data_append| replace:: ``data_append``
.. _data_append: https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic-api/data/data_append.rst
.. |model_generate| replace:: ``model_generate``
.. _model_generate: https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic-api/model/model_generate.rst
.. |model_predict| replace:: ``model_predict``
.. _model_predict: https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic-api/predict/model_predict.rst
