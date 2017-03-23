=================
Unit Test: pytest
=================

This project implements `unit testing <https://en.wikipedia.org/wiki/Unit_testing>`_,
to validate logic in a consistent fashion. These unit tests have been automated within
corresponding travis `builds <https://travis-ci.org/jeff1evesque/machine-learning>`_,
using a series of docker containers, connected via a common docker network:

- |.travis.yml#L101-L120|_
- |default.dockerfile|_
- |database.dockerfile|_
- |redis.dockerfile|_
- |webserver.dockerfile|_

Current unit tests cover the following sessions:

- ``data_new``
- ``data_append``
- ``model_predict``
- ``model_generate``

As well as the following authentication specific cases:

- account registration
- crypto function
- user login
- user logout
- password validation

The unit tests are automatically executed upon submitting a pull request. However,
the same tests can be run manually, since both implementations execute the same
|unit-tests|_ bash script:

.. code:: bash

    vagrant@trusty64:/vagrant/utility$ ./unit-tests
    ...
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.6, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
    rootdir: /var/machine-learning/test/live_server, inifile: pytest.ini
    plugins: flask-0.10.0, cov-2.4.0
    collected 21 items

    test/live_server/authentication/pytest_account_registration.py .
    test/live_server/authentication/pytest_crypto.py .
    test/live_server/authentication/pytest_user_login.py .
    test/live_server/authentication/pytest_user_logout.py .
    test/live_server/authentication/pytest_validate_password.py .
    test/live_server/programmatic_interface/dataset_url/pytest_svm_dataset_url.py ....
    test/live_server/programmatic_interface/dataset_url/pytest_svr_dataset_url.py ....
    test/live_server/programmatic_interface/file_upload/pytest_svm_file_upload.py ....
    test/live_server/programmatic_interface/file_upload/pytest_svr_file_upload.py ....

    ---------- coverage: platform linux2, python 2.7.6-final-0 -----------
    Name                                                                            Stmts   Miss  Cover
    ---------------------------------------------------------------------------------------------------
    __init__.py                                                                         0      0   100%
    app.py                                                                             12     12     0%
    brain/__init__.py                                                                   0      0   100%
    brain/cache/__init__.py                                                             0      0   100%
    brain/cache/cache_hset.py                                                          22     14    36%
    brain/cache/cache_model.py                                                         36     26    28%
    brain/cache/redis_query.py                                                         87     77    11%
    brain/cache/redis_session.py                                                       54     54     0%
    brain/cache/redis_settings.py                                                      14     10    29%
    brain/converter/__init__.py                                                         0      0   100%
    brain/converter/calculate_md5.py                                                    9      9     0%
    brain/converter/convert_dataset.py                                                 45     29    36%
    brain/converter/crypto.py                                                          45      6    87%
    brain/converter/dataset/__init__.py                                                 0      0   100%
    brain/converter/dataset/svm_csv_converter.py                                       38     38     0%
    brain/converter/dataset/svm_json_converter.py                                      58     10    83%
    brain/converter/dataset/svm_xml_converter.py                                       27     27     0%
    brain/converter/dataset/svr_csv_converter.py                                       38     38     0%
    brain/converter/dataset/svr_json_converter.py                                      58     10    83%
    brain/converter/dataset/svr_xml_converter.py                                       30     30     0%
    brain/converter/restructure_settings.py                                            45     25    44%
    brain/converter/serialize_model.py                                                 12      7    42%
    brain/database/__init__.py                                                          0      0   100%
    brain/database/db_query.py                                                         55     24    56%
    brain/database/db_settings.py                                                      19     13    32%
    brain/database/retrieve_account.py                                                 48     13    73%
    brain/database/retrieve_entity.py                                                  18      7    61%
    brain/database/retrieve_feature.py                                                 32      9    72%
    brain/database/retrieve_model_type.py                                              18      7    61%
    brain/database/retrieve_session.py                                                 22     22     0%
    brain/database/save_account.py                                                     18      7    61%
    brain/database/save_entity.py                                                      25      7    72%
    brain/database/save_feature.py                                                     35      9    74%
    brain/database/save_observation.py                                                 25      7    72%
    brain/load_data.py                                                                 89     29    67%
    brain/schema/__init__.py                                                            0      0   100%
    brain/schema/jsonschema_definition.py                                              13      5    62%
    brain/session/__init__.py                                                           0      0   100%
    brain/session/base.py                                                              27     16    41%
    brain/session/base_data.py                                                         60     35    42%
    brain/session/data/__init__.py                                                      0      0   100%
    brain/session/data/dataset_to_dict.py                                              48     11    77%
    brain/session/data/save_dataset.py                                                 11      4    64%
    brain/session/data/save_entity.py                                                  13     13     0%
    brain/session/data/save_feature_count.py                                            8      4    50%
    brain/session/data/save_observation_label.py                                       19      5    74%
    brain/session/data/validate_file_extension.py                                      37     22    41%
    brain/session/data_append.py                                                       15      8    47%
    brain/session/data_new.py                                                          16      8    50%
    brain/session/model/__init__.py                                                     0      0   100%
    brain/session/model/sv.py                                                          64     16    75%
    brain/session/model_generate.py                                                    20      9    55%
    brain/session/model_predict.py                                                     14      7    50%
    brain/session/predict/__init__.py                                                   0      0   100%
    brain/session/predict/sv.py                                                        21      5    76%
    brain/validator/__init__.py                                                         0      0   100%
    brain/validator/validate_dataset.py                                                15      8    47%
    brain/validator/validate_file_extension.py                                         62     40    35%
    brain/validator/validate_password.py                                               43      4    91%
    brain/validator/validate_settings.py                                               43     18    58%
    factory.py                                                                         44      8    82%
    interface/__init__.py                                                               0      0   100%
    interface/views.py                                                                132     97    27%
    log/__init__.py                                                                     0      0   100%
    log/logger.py                                                                      84     50    40%
    puppet/__init__.py                                                                  0      0   100%
    puppet/environment/__init__.py                                                      0      0   100%
    puppet/environment/docker/__init__.py                                               0      0   100%
    puppet/environment/docker/modules/__init__.py                                       0      0   100%
    puppet/environment/docker/modules/mariadb/__init__.py                               0      0   100%
    puppet/environment/docker/modules/mariadb/scripts/__init__.py                       0      0   100%
    puppet/environment/docker/modules/mariadb/scripts/setup_tables.py                  50     50     0%
    puppet/environment/vagrant/__init__.py                                              0      0   100%
    puppet/environment/vagrant/modules/__init__.py                                      0      0   100%
    puppet/environment/vagrant/modules/mariadb/__init__.py                              0      0   100%
    puppet/environment/vagrant/modules/mariadb/scripts/__init__.py                      0      0   100%
    puppet/environment/vagrant/modules/mariadb/scripts/setup_tables.py                 50     50     0%
    test/live_server/authentication/pytest_account_registration.py                     21      3    86%
    test/live_server/authentication/pytest_crypto.py                                   15      2    87%
    test/live_server/authentication/pytest_user_login.py                               20      3    85%
    test/live_server/authentication/pytest_user_logout.py                              13      1    92%
    test/live_server/authentication/pytest_validate_password.py                        16      2    88%
    test/live_server/conftest.py                                                       12      2    83%
    test/live_server/programmatic_interface/dataset_url/pytest_svm_dataset_url.py      49      0   100%
    test/live_server/programmatic_interface/dataset_url/pytest_svr_dataset_url.py      43      0   100%
    test/live_server/programmatic_interface/file_upload/pytest_svm_file_upload.py      49      0   100%
    test/live_server/programmatic_interface/file_upload/pytest_svr_file_upload.py      43      0   100%
    ---------------------------------------------------------------------------------------------------
    TOTAL                                                                            2224   1082    51%


    ========================== 21 passed in 63.84 seconds ==========================

**Note:** future releases (i.e. milestone `1.0 <https://github.com/jeff1evesque/machine-learning/milestones/1.0>`_),
will include more granular unit tests, or more logical ordered, such that particular
sets of unit tests will conditionally run upon execution of test dependencies.

It is important to understand that building the corresponding docker containers
needed for the unit tests, is resource intensive, also with respect to the harddisk.
Therefore, the `unit-tests` bash script, properly `cleans-up <https://github.com/jeff1evesque/machine-learning/blob/b9fdb85c55fa99992ed78cba538d5ef7f3c62c64/utility/unit-tests#L75-L89>`_
after it's execution. Additionally, given that the vagrant development environment,
has not exceeded harddisk limitations, all executions should have necessary space by
default, from an initial ``vagrant up xxx``. For example, during the execution of the
`unit-tests` (before clean-up), the harddisk partitions were as follows:

.. code:: bash
    vagrant@trusty64:/vagrant/utility$ df -h
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

After the |unit-tests|_ successfully execute, the harddisk should be reduced,
as a part of it's intrinsic clean-up:

.. code:: bash
    vagrant@trusty64:/vagrant/utility$ df -h
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

Therefore, it is fair to assume that if the main host had adequate resources
to build this application:

- harddisk
- memory
- cpu
- network speed

Then, the unit tests should be re-runnable, meaning multiple executions of the
|unit-tests|_ bash script, should run without a problem. More information regarding
`hardware architecture <https://github.com/jeff1evesque/machine-learning/blob/master/documentation/hardware/architecture.st>`_,
and resources can be reviewed to determine the best combination for a given situation.

**Note:** every script within this repository, with the
`exception <https://github.com/jeff1evesque/machine-learning/issues/2234#issuecomment-158850974>`_
of puppet (erb) `templates <https://github.com/jeff1evesque/machine-learning/tree/master/puppet/template>`_,
and a handful of open source libraries, have been `linted <https://en.wikipedia.org/wiki/Lint_%28software%29>`_
via |.travis.yml|_

.. |.travis.yml| replace:: ``.travis.yml``
.. _.travis.yml: https://github.com/jeff1evesque/machine-learning/blob/master/.travis.yml
.. |.travis.yml#L101-L120| replace:: ``.travis.yml#L101-L120``
.. _.travis.yml#L101-L120: https://github.com/jeff1evesque/machine-learning/blob/e83f4222a9de11fcd839d6b3e789d63bab82e093/.travis.yml#L101-L120
.. |default.dockerfile| replace:: ``default.dockerfile``
.. _default.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/default.dockerfile
.. |database.dockerfile| replace:: ``database.dockerfile``
.. _database.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/database.dockerfile
.. |redis.dockerfile| replace:: ``redis.dockerfile``
.. _redis.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/redis.dockerfile
.. |webserver.dockerfile| replace:: ``webserver.dockerfile``
.. _webserver.dockerfile: https://github.com/jeff1evesque/machine-learning/blob/master/webserver.dockerfile
.. |unit-tests| replace:: ``unit-tests``
.. _unit-tests: https://github.com/jeff1evesque/machine-learning/blob/master/utility/unit-tests
