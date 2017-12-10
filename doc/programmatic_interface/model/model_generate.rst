==============
Model Generate
==============

The ``model_generate`` session, is an implementation that generates a desired model,
using previously uploaded dataset(s), via either the ``data_new``, or the ``data_append``
session. The required attributes, for the corresponding session, is sent to the
``/load-data`` endpoint, which is demonstrated as follows:

- `svm example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svm/dataset_url/svm-model-generate.json>`_
- `svr example <https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/svr/dataset_url/svr-model-generate.json>`_

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

- ``collection``: collection of dataset documents, used to generate a model

- ``session_type``: corresponds to one of the following session types:

  - ``data_new``
  - ``data_append``
  - ``model_generate``
  - ``model_predict``

- ``model_type``: the type of model to perform on:

  - ``svm``
  - ``svr``

- ``sv_kernel_type``: the type of kernel to apply to the support vector ``model_type``:

  -  ``linear``
  -  ``polynomial``
  -  ``rbf``
  -  ``sigmoid``

- ``penalty``: penalty parameter C of the error term, must be a float value:

``C=1``
-------

.. code:: python
    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=.01, C=1)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize the decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33807641-f6ca9800-dda7-11e7-84d9-137c5283f8b4.png
   :alt: svm penalty c=1

``C=10``
--------

.. code:: python
    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=.01, C=10)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize the decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33807649-0ecc4296-dda8-11e7-96b3-4eb92c8bb4db.png
   :alt: svm penalty c=10

``C=10000``
-----------

.. code:: python
    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=.01, C=10000)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize the decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33807657-27872dd2-dda8-11e7-80c0-e73e7a5b144b.png
   :alt: svm penalty c=10000
