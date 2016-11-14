================
Unit Test: pytest
================

This project implements `unit testing <https://en.wikipedia.org/wiki/Unit_testing>`_,
to validate logic in a consistent fashion. Currently, only `high-level <https://github.com/jeff1evesque/machine-learning/tree/master/test/live_server>`_
unit tests have been defined. These unit tests have been automated within corresponding
travis `builds <https://travis-ci.org/jeff1evesque/machine-learning>`_, using
a series of docker containers, connected via a common docker network:

- |.travis.yml|
- ```default.dockerfile`` <https://github.com/jeff1evesque/machine-learning/blob/master/default.dockerfile>`_
- ```database.dockerfile`` <https://github.com/jeff1evesque/machine-learning/blob/master/database.dockerfile>`_
- ```redis.dockerfile`` <https://github.com/jeff1evesque/machine-learning/blob/master/redis.dockerfile>`_
- ```webserver.dockerfile`` <https://github.com/jeff1evesque/machine-learning/blob/master/webserver.dockerfile>`_

.. |.travis.yml| replace:: ``.travis.yml``
.. .travis.yml: https://github.com/jeff1evesque/machine-learning/blob/e83f4222a9de11fcd839d6b3e789d63bab82e093/.travis.yml#L101-L120

Current unit tests cover the following sessions:

- ``data_new``
- ``data_append``
- ``model_predict``
- ``model_generate``

which can be executed `manually <https://github.com/jeff1evesque/machine-learning/tree/master/test/manual>`_
as follows:

.. code:: bash

    $ cd /path/to/machine-learning/
    $ vagrant up
    $ vagrant ssh
    vagrant@vagrant-ubuntu-trusty-64:~$ (cd /vagrant/test && pytest manual)
    ========================================= test session starts ==========================================
    platform linux2 -- Python 2.7.6, pytest-3.0.3, py-1.4.31, pluggy-0.4.0
    rootdir: /vagrant/test/manual, inifile: pytest.ini
    plugins: flask-0.10.0
    collected 20 items

    manual/configure_database.py .
    manual/configure_redis.py .
    manual/authentication/pytest_crypto.py .
    manual/authentication/pytest_validate_password.py .
    manual/programmatic_interface/dataset_url/pytest_svm_dataset_url.py ....
    manual/programmatic_interface/dataset_url/pytest_svr_dataset_url.py ....
    manual/programmatic_interface/file_upload/pytest_svm_file_upload.py ....
    manual/programmatic_interface/file_upload/pytest_svr_file_upload.py ....

    ====================================== 20 passed in 51.27 seconds ======================================

**Note:** future releases (i.e. milestone `1.0 <https://github.com/jeff1evesque/machine-learning/milestones/1.0>`_),
will include more granular unit tests.

**Note:** every script within this repository, with the
`exception <https://github.com/jeff1evesque/machine-learning/issues/2234#issuecomment-158850974>`_
of puppet (erb) `templates <https://github.com/jeff1evesque/machine-learning/tree/master/puppet/template>`_,
and a handful of open source libraries, have been `linted <https://en.wikipedia.org/wiki/Lint_%28software%29>`_
via ```.travis.yml`` <https://github.com/jeff1evesque/machine-learning/blob/master/.travis.yml>`_.
