===============
Unit Test: Jest
===============

Jest is used to perform unit testing against our reactjs frontend code. Specifically,
our `package.json`, defines a corresponding `script`, to execute the set of unit tests:

.. code:: bash

    root@browserify:/var/machine-learning/src# npm run test

**Note:** it is important to remember to run the above command in the same directory,
containing the `package.json`, within the `browserify` docker container.

This frontend testing can be executed manually, as indicated above. However, it is also
implemented within our travis ci. Therefore, each pull request, will verify the integrity
of the reactjs frontend code.