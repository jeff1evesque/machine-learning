==============
Result Arbiter
==============

The result arbiter provides an interface to perform the following tasks:

- store prediction: corresponds to the ``/save-prediction`` endpoint

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/results/save-prediction.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/results/save-prediction.json>`_

- retrieve prediction: corresponds to the ``/retrieve-prediction`` endpoint

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/results/retrieve-prediction.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/results/retrieve-prediction.json>`_

- retrieve prediction titles: corresponds to the ``/retrieve-prediction-titles`` endpoint

  - `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/results/retrieve-titles.json>`_
  - `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/results/retrieve-titles.json>`_
  - `combined example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/combined/results/retrieve-titles.json>`_

**Note:** the content of each of the above files, can be substituted for
the ``data`` attribute.

The following properties define the above ``data`` attributes:

- ``model_type``: corresponds to the desired model type:

  - ``all``: pertains to all stored model types
  - ``svm``: pertains only for the support vector machine model type
  - ``svr``: pertains only for the suppport vector regression model type
