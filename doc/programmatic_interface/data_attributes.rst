===============
Data Attributes
===============

The programmatic-api is intended to provide the same functionality as the web-interface,
with the exception that corresponding commands, are contained within various attributes,
encapsulated into a ``POST`` request, and sent to its respective url endpoint.

The following are corresponding endpoints, currently supported by this application:

- ``/load-data``: which supports the following sessions:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``/save-prediction``: stores a generated prediction

- ``/retrieve-prediction``: retrieves the following prediction attributes:

  - result: pertains to all ``model_type``
  - classes: pertains only to svm ``model_type``
  - decision function: pertains only to svm ``model_type``
  - probabilities: pertains only to svm ``model_type``
  - coefficient of determination: pertains only to svr ``model_type``
