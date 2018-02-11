=====
Gamma
=====

The below gamma cases, are predicated on the following:

.. code:: python

    # classifying packages
    import numpy as np
    from sklearn.svm import SVC

    # visualizer packages
    from matplotlib.colors import ListedColormap
    import matplotlib.pyplot as plt
    import warnings

    def versiontuple(v):
        return tuple(map(int, (v.split('.'))))

    def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
        # setup marker generator and color map
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # plot the decision surface
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(
            np.arange(
                x1_min,
                x1_max,
                resolution
            ),
            np.arange(x2_min, x2_max, resolution)
        )
        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(
                x=X[y == cl, 0],
                y=X[y == cl, 1],
                alpha=0.8,
                c=cmap(idx),
                marker=markers[idx],
                label=cl
            )

        # highlight test samples
        if test_idx:
            # plot all samples
            if not versiontuple(np.__version__) >= versiontuple('1.9.0'):
                X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
                warnings.warn('Please update to NumPy 1.9.0 or newer')
            else:
                X_test, y_test = X[test_idx, :], y[test_idx]

            plt.scatter(
                X_test[:, 0],
                X_test[:, 1],
                c='',
                alpha=1.0,
                linewidths=1,
                marker='o',
                s=55,
                label='test set'
            )

    # generate sample data
    np.random.seed(0)
    X_xor = np.random.randn(200, 2)
    y_xor = np.logical_xor(
        X_xor[:, 0] > 0,
        X_xor[:, 1] > 0
    )
    y_xor = np.where(y_xor, 1, -1)

**Note:** concepts on this page, have been integrated into the `mlxtend <http://rasbt.github.io/mlxtend/>`_ library.

Gamma = 1.0
-----------

.. code:: python

    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=1, C=1)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33811284-4f70e892-dddf-11e7-9045-55b4787d2b76.png
   :alt: svm gamma=1

Gamma = 10.0
------------

.. code:: python

    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=10, C=1)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33811290-5ddb183a-dddf-11e7-8deb-65492b2c68be.png
   :alt: svm gamma=10

Gamma = 100.0
-------------

.. code:: python

    # create SVC classifier
    svm = SVC(kernel='rbf', random_state=0, gamma=100, C=1)

    # train classifier
    svm.fit(X_xor, y_xor)

    # visualize decision boundaries
    plot_decision_regions(X_xor, y_xor, classifier=svm)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

.. image:: https://user-images.githubusercontent.com/2907085/33811297-91a13c08-dddf-11e7-8850-f1d53a783a4e.png
   :alt: svm gamma=100
