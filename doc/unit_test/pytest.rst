=================
Unit Test: pytest
=================

This project implements `unit testing <https://en.wikipedia.org/wiki/Unit_testing>`_,
to validate logic in a consistent fashion. This is done through an automated process
via travis `builds <https://travis-ci.org/jeff1evesque/machine-learning>`_, when code
is submitted through a `pull request <https://github.com/jeff1evesque/machine-learning/pulls>`_.
Essentially, a series of docker containers, connected under a common `docker network <https://docs.docker.com/engine/userguide/networking/>`_,
are created by the `travis ci <https://travis-ci.org/jeff1evesque/machine-learning>`_:

- |unit-tests#L47-L50|_
- |default.dockerfile|_
- |database.dockerfile|_
- |redis.dockerfile|_
- |webserver.dockerfile|_

This allows unit tests to cover the following sessions:

- ``data_new``
- ``data_append``
- ``model_predict``
- ``model_generate``

As well as the following authentication cases:

- account registration
- crypto function
- user login
- user logout
- password validation

However, both the automated, and manual unit tests, implement the same |unit-tests|_
bash script. Therefore, the manual unit tests can be implemented as follows:

.. code:: bash

    vagrant@trusty64:/vagrant/test$ ./unit-tests
    ...
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.6, pytest-3.2.3, py-1.4.34, pluggy-0.4.0
    rootdir: /var/machine-learning/test/live_server, inifile: pytest.ini
    plugins: flask-0.10.0, cov-2.4.0
    collected 57 items                                                              
    test/live_server/1_authentication/pytest_1_crypto.py .
    test/live_server/1_authentication/pytest_2_account_registration.py .
    test/live_server/1_authentication/pytest_3_validate_password.py .
    test/live_server/1_authentication/pytest_4_user_login.py .
    test/live_server/1_authentication/pytest_5_user_logout.py .
    test/live_server/1_authentication/pytest_6_user_session.py .
    test/live_server/2_database/pytest_svm_dbmax.py ..........
    test/live_server/2_database/pytest_svr_dbmax.py ..........
    test/live_server/3_programmatic_interface/dataset_url/pytest_bagc_dataset_url.py ....
    test/live_server/3_programmatic_interface/dataset_url/pytest_svm_dataset_url.py ....
    test/live_server/3_programmatic_interface/dataset_url/pytest_svr_dataset_url.py ....
    test/live_server/3_programmatic_interface/file_upload/pytest_bagc_file_upload.py ....
    test/live_server/3_programmatic_interface/file_upload/pytest_svm_file_upload.py ....
    test/live_server/3_programmatic_interface/file_upload/pytest_svr_file_upload.py ....
    test/live_server/3_programmatic_interface/results/pytest_1_svm_prediction.py ...
    test/live_server/3_programmatic_interface/results/pytest_2_svr_prediction.py ...
    test/live_server/3_programmatic_interface/results/pytest_3_all_prediction_titles.py .

    ---------- coverage: platform linux2, python 2.7.6-final-0 -----------
    Name                                                                                  Stmts   Miss  Cover
    ---------------------------------------------------------------------------------------------------------
    __init__.py                                                                               0      0   100%
    app.py                                                                                   12     12     0%
    brain/__init__.py                                                                         0      0   100%
    brain/cache/__init__.py                                                                   0      0   100%
    brain/cache/hset.py                                                                      22     14    36%
    brain/cache/model.py                                                                     34     24    29%
    brain/cache/query.py                                                                     87     77    11%
    brain/cache/session.py                                                                   51     32    37%
    brain/cache/settings.py                                                                  14     10    29%
    brain/converter/__init__.py                                                               0      0   100%
    brain/converter/crypto.py                                                                45      6    87%
    brain/converter/format/__init__.py                                                        0      0   100%
    brain/converter/format/csv2dict.py                                                       21     21     0%
    brain/converter/format/xml2dict.py                                                       19     19     0%
    brain/converter/md5.py                                                                    9      9     0%
    brain/converter/model.py                                                                 12      7    42%
    brain/converter/operation.py                                                             45     45     0%
    brain/converter/settings.py                                                              50     50     0%
    brain/database/__init__.py                                                                0      0   100%
    brain/database/account.py                                                                53     15    72%
    brain/database/dataset.py                                                                16      6    63%
    brain/database/entity.py                                                                 60     22    63%
    brain/database/model_type.py                                                             17      7    59%
    brain/database/prediction.py                                                             89     19    79%
    brain/database/query.py                                                                 125     59    53%
    brain/database/session.py                                                                30     20    33%
    brain/database/settings.py                                                               46     24    48%
    brain/load_data.py                                                                       83     37    55%
    brain/schema/__init__.py                                                                  0      0   100%
    brain/schema/dataset.py                                                                   7      3    57%
    brain/schema/session.py                                                                  13      5    62%
    brain/session/__init__.py                                                                 0      0   100%
    brain/session/base.py                                                                    25     15    40%
    brain/session/base_data.py                                                               61     25    59%
    brain/session/data/__init__.py                                                            0      0   100%
    brain/session/data/dataset.py                                                            70     49    30%
    brain/session/data_append.py                                                             29     12    59%
    brain/session/data_new.py                                                                27     10    63%
    brain/session/model/__init__.py                                                           0      0   100%
    brain/session/model/adabooster.py                                                        50     50     0%
    brain/session/model/bagger.py                                                            59     18    69%
    brain/session/model/sv.py                                                                44      8    82%
    brain/session/model_generate.py                                                          26     10    62%
    brain/session/model_predict.py                                                           20      9    55%
    brain/session/predict/__init__.py                                                         0      0   100%
    brain/session/predict/adaboost.py                                                        18     18     0%
    brain/session/predict/bag.py                                                             27      8    70%
    brain/session/predict/sv.py                                                              22      5    77%
    brain/validator/__init__.py                                                               0      0   100%
    brain/validator/dataset.py                                                               16     16     0%
    brain/validator/email.py                                                                  7      3    57%
    brain/validator/password.py                                                              43      4    91%
    brain/validator/settings.py                                                              41     18    56%
    factory.py                                                                               55     16    71%
    interface/__init__.py                                                                     0      0   100%
    interface/views.py                                                                      248    143    42%
    log/__init__.py                                                                           0      0   100%
    log/logger.py                                                                            84     84     0%
    puppet/__init__.py                                                                        0      0   100%
    puppet/environment/__init__.py                                                            0      0   100%
    puppet/environment/docker/__init__.py                                                     0      0   100%
    puppet/environment/docker/modules/__init__.py                                             0      0   100%
    puppet/environment/docker/modules/mariadb/__init__.py                                     0      0   100%
    puppet/environment/docker/modules/mariadb/scripts/__init__.py                             0      0   100%
    puppet/environment/docker/modules/mariadb/scripts/setup_tables.py                        40     40     0%
    puppet/environment/vagrant/__init__.py                                                    0      0   100%
    puppet/environment/vagrant/modules/__init__.py                                            0      0   100%
    puppet/environment/vagrant/modules/mariadb/__init__.py                                    0      0   100%
    puppet/environment/vagrant/modules/mariadb/scripts/__init__.py                            0      0   100%
    puppet/environment/vagrant/modules/mariadb/scripts/setup_tables.py                       40     40     0%
    test/live_server/1_authentication/pytest_1_crypto.py                                     15      2    87%
    test/live_server/1_authentication/pytest_2_account_registration.py                       21      3    86%
    test/live_server/1_authentication/pytest_3_validate_password.py                          16      2    88%
    test/live_server/1_authentication/pytest_4_user_login.py                                 19      3    84%
    test/live_server/1_authentication/pytest_5_user_logout.py                                12      0   100%
    test/live_server/1_authentication/pytest_6_user_session.py                               16      1    94%
    test/live_server/2_database/pytest_svm_dbmax.py                                         102      0   100%
    test/live_server/2_database/pytest_svr_dbmax.py                                         103      0   100%
    test/live_server/3_programmatic_interface/dataset_url/pytest_bagc_dataset_url.py         37      0   100%
    test/live_server/3_programmatic_interface/dataset_url/pytest_svm_dataset_url.py          52      0   100%
    test/live_server/3_programmatic_interface/dataset_url/pytest_svr_dataset_url.py          42      0   100%
    test/live_server/3_programmatic_interface/file_upload/pytest_bagc_file_upload.py         36      0   100%
    test/live_server/3_programmatic_interface/file_upload/pytest_svm_file_upload.py          52      0   100%
    test/live_server/3_programmatic_interface/file_upload/pytest_svr_file_upload.py          42      0   100%
    test/live_server/3_programmatic_interface/results/pytest_1_svm_prediction.py             64     17    73%
    test/live_server/3_programmatic_interface/results/pytest_2_svr_prediction.py             62     17    73%
    test/live_server/3_programmatic_interface/results/pytest_3_all_prediction_titles.py      33      7    79%
    test/live_server/conftest.py                                                             12      2    83%
    ---------------------------------------------------------------------------------------------------------
    TOTAL                                                                                  2748   1198    56%
    =============================== warnings summary ===============================
    3_programmatic_interface/results/pytest_1_svm_prediction.py::test_save_prediction
      /var/machine-learning/brain/database/query.py:281: Warning: Data truncated for column 'probability' at row 1
        self.cursor.execute(statement, sql_args)
      /var/machine-learning/brain/database/query.py:281: Warning: Data truncated for column 'decision_function' at row 1
        self.cursor.execute(statement, sql_args)

    3_programmatic_interface/results/pytest_2_svr_prediction.py::test_save_prediction
      /var/machine-learning/brain/database/query.py:281: Warning: Data truncated for column 'r2' at row 1
        self.cursor.execute(statement, sql_args)

    -- Docs: http://doc.pytest.org/en/latest/warnings.html
    =================== 57 passed, 3 warnings in 120.34 seconds ====================

**Note:** future releases (i.e. milestone `1.0 <https://github.com/jeff1evesque/machine-learning/milestones/1.0>`_),
will include more granular unit tests, or better logical order, such that particular
sets of unit tests will conditionally run, upon successful execution of dependencies.

It is important to understand that building the corresponding docker containers
needed for the unit tests, is resource intensive, also with respect to the harddisk.
Therefore, the |unit-tests|_ will `clean-up <https://github.com/jeff1evesque/machine-learning/blob/d3ecbd53299d082ceffe77d28875743a923fec1b/test/unit-tests#L75-L89>`_
after it's execution. Additionally, given that the vagrant development environment,
has not exceeded harddisk limitations, all executions should have necessary space by
default, from an initial ``vagrant up xxx``. For example, during the execution of the
`unit-tests` (before clean-up), the harddisk partitions should be as follows:

.. code:: bash

    vagrant@trusty64:/vagrant/test$ df -h
    Filesystem                                                     Size  Used Avail Use% Mounted on
    udev                                                           486M  4.0K  486M   1% /dev
    tmpfs                                                          100M  644K   99M   1% /run
    /dev/sda1                                                      7.8G  4.0G  3.4G  55% /
    none                                                           4.0K     0  4.0K   0% /sys/fs/cgroup
    none                                                           5.0M     0  5.0M   0% /run/lock
    none                                                           497M  636K  496M   1% /run/shm
    none                                                           100M     0  100M   0% /run/user
    vagrant                                                        466G  145G  322G  31% /vagrant
    tmp_vagrant-puppet_environments                                466G  145G  322G  31% /tmp/vagrant-puppet/environments
    tmp_vagrant-puppet_modules-3c00084ae9953309c24252b2dd2bf5cd    466G  145G  322G  31% /tmp/vagrant-puppet/modules-3c00084ae9953309c24252b2dd2bf5cd
    tmp_vagrant-puppet_modules-044f8ea6fe024da4abbd7bbb8407a17e    466G  145G  322G  31% /tmp/vagrant-puppet/modules-044f8ea6fe024da4abbd7bbb8407a17e
    tmp_vagrant-puppet_manifests-3def0df79d1c452de6a52de4d163c7cc  466G  145G  322G  31% /tmp/vagrant-puppet/manifests-3def0df79d1c452de6a52de4d163c7cc

After the |unit-tests|_ successfully executes, the harddisk should be reduced,
as a part of it's intrinsic clean-up:

.. code:: bash

    vagrant@trusty64:/vagrant/test$ df -h
    Filesystem                                                     Size  Used Avail Use% Mounted on
    udev                                                           486M  4.0K  486M   1% /dev
    tmpfs                                                          100M  548K   99M   1% /run
    /dev/sda1                                                      7.8G  2.3G  5.1G  32% /
    none                                                           4.0K     0  4.0K   0% /sys/fs/cgroup
    none                                                           5.0M     0  5.0M   0% /run/lock
    none                                                           497M     0  497M   0% /run/shm
    none                                                           100M     0  100M   0% /run/user
    vagrant                                                        466G  145G  322G  31% /vagrant
    tmp_vagrant-puppet_environments                                466G  145G  322G  31% /tmp/vagrant-puppet/environments
    tmp_vagrant-puppet_modules-3c00084ae9953309c24252b2dd2bf5cd    466G  145G  322G  31% /tmp/vagrant-puppet/modules-3c00084ae9953309c24252b2dd2bf5cd
    tmp_vagrant-puppet_modules-044f8ea6fe024da4abbd7bbb8407a17e    466G  145G  322G  31% /tmp/vagrant-puppet/modules-044f8ea6fe024da4abbd7bbb8407a17e
    tmp_vagrant-puppet_manifests-3def0df79d1c452de6a52de4d163c7cc  466G  145G  322G  31% /tmp/vagrant-puppet/manifests-3def0df79d1c452de6a52de4d163c7cc

Therefore, it is fair to assume that if the main host has adequate resources
to build this application:

- harddisk
- memory
- cpu
- network speed

Then, the unit tests should be re-runnable, meaning multiple successive executions
of the |unit-tests|_ bash script, should run without a problem. More information
regarding `hardware architecture <https://github.com/jeff1evesque/machine-learning/blob/master/documentation/hardware/architecture.st>`_,
and resources can be reviewed to determine the best combination for a given situation.

**Note:** every script within this repository, with the
`exception <https://github.com/jeff1evesque/machine-learning/issues/2234#issuecomment-158850974>`_
of puppet (erb) `templates <https://github.com/jeff1evesque/machine-learning/tree/master/puppet/template>`_,
and a handful of open source libraries, have been `linted <https://en.wikipedia.org/wiki/Lint_%28software%29>`_
via |.travis.yml|_

.. |.travis.yml| replace:: ``.travis.yml``
.. _.travis.yml: https://github.com/jeff1evesque/machine-learning/blob/master/.travis.yml
.. |unit-tests#L47-L50| replace:: ``unit-tests#L47-L50``
.. _unit-tests#L47-L50: https://github.com/jeff1evesque/machine-learning/blob/d3ecbd53299d082ceffe77d28875743a923fec1b/test/unit-tests#L47-L50
.. |default.dockerfile| replace:: ``default.dockerfile``
.. _default.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/default.dockerfile
.. |database.dockerfile| replace:: ``database.dockerfile``
.. _database.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/database.dockerfile
.. |redis.dockerfile| replace:: ``redis.dockerfile``
.. _redis.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/redis.dockerfile
.. |webserver.dockerfile| replace:: ``webserver.dockerfile``
.. _webserver.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/webserver.dockerfile
.. |unit-tests| replace:: ``unit-tests``
.. _unit-tests: https://github.com/jeff1evesque/machine-learning/blob/master/test/unit-tests
