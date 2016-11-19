===============
Data Attributes
===============

-  `SVM
   datasets <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm>`_

   -  `dataset url <https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/programmatic_interface/svm/dataset_url>`_
   -  `file upload <https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/programmatic_interface/svm/file_upload>`_

-  `SVR
   datasets <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr>`_

   -  `dataset url <https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/programmatic_interface/svr/dataset_url>`_
   -  `file upload <https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/programmatic_interface/svr/file_upload>`_

**Note:** the content of each of the above files, can be substituted for
the ``data`` attribute.

The following (non-exhaustive) properties define the implemented
``data`` attribute:

-  ``model_id``: the numeric id value, of the generated model in the
   nosql datastore
-  ``model_type``: corresponds to the desired model type, which can be
   one of the following:
-  ``classification``
-  ``regression``
-  ``session_id``: the numeric id value, that represents the dataset
   stored in the sql database.
-  ``dataset_type``: corresponds to one of the following types:
-  ``dataset_url``: indication that the supplied dataset will be url
   references
-  ``file_upload``: indication that the supplied dataset(s) will be
   defined as a json string within the ``dataset`` attribute
-  ``session_type``: corresponds to one of the following session types:
-  ``data_new``
-  ``data_append``
-  ``model_generate``
-  ``model_predict``
-  ``svm_dataset_type``: corresponds to one of the following dataset
   types:
-  ``json_string``: indicate that the dataset is being sent via a
   ``post`` request
-  ``sv_kernel_type``: the type of kernel to apply to the support vector
   ``model_type``:
-  ``linear``
-  ``polynomial``
-  ``rbf``
-  ``sigmoid``
-  ``prediction_input[]``: an array of prediction input, supplied to the
   generated model to compute a prediction
