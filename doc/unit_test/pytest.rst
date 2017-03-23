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
    cf4d9e79e5c5
    f62ee18006c9
    913d3e21b8df
    cf4d9e79e5c5
    4db08379cb49
    f62ee18006c9
    bf4c7d6564ad
    Untagged: container-webserver:latest
    Deleted: sha256:956590f0b1898e72ae4c470ef03484c78c6e7744071d3c15356a86b7f7f0d4ba
    Deleted: sha256:61edf5ba00145275760f705a0ce9d36e4cec447e6f2b75f86e669b11e2e27b86
    Deleted: sha256:433d8d86d024581952aa146f0d7843bcb38c98f555af195b8f472b11a7c8a180
    Deleted: sha256:0bb2dfb1ad46d701415b370db0d88b7067a474788271fb11cb59507b3d8ce816
    Untagged: container-database:latest
    Deleted: sha256:5830fe25e6e3bc6b98d9cad6f63f2a263f64c2241ed15dafb69660f3cf0a9475
    Deleted: sha256:d48cf3c0d3548bf124b6f0451fbd46cd149917e7975775a0a406ce8249333275
    Deleted: sha256:6148f71a88cebde390c32876ac50b02400eb8d5e441e47da92d75bee88c0966a
    Untagged: container-redis:latest
    Deleted: sha256:fc00b75a45be257a5cdf2eb62e1ddd6a0c087767896cffa2f2a0b12ddbaa70d7
    Deleted: sha256:47e6b2f3f025bedaaa6ad431f345d0ce471f9933acbde2c96b6f085758a3e27b
    Deleted: sha256:7f85f5e32799a39f098075294311fc86d7652ca69f20a2d266f26d4062837ed2
    Deleted: sha256:92834f13806ec8e2ed3ee9fd4e35721f354762741fda68307f59f30eb8c478be
    Deleted: sha256:be536aa80786a6e895636e1342351127f6e8ae9b687cc3ce1f41d6ec6f62a342
    Deleted: sha256:d0e031eaef4ffb1aad6d5095ddf174c74b0565b59ea36e2daab51b51bd471e6f
    Untagged: container-default:latest
    Deleted: sha256:3138f13ce426b3a830bca4733dc0643861cb50264bcbc4c1b91b74ffc163e667
    Deleted: sha256:cd25785ea124f0fe735965fc81146bfebb4e3d75750881c953b153d417023f9c
    Deleted: sha256:59ee68c734c9d308eee36cba09e0e0bac60edaee65a305368cc1a20faaa814b4
    Deleted: sha256:84b38cd1ae12faeda32cfcfc11564087e4241a13d42fde642bac877d306ed558
    Deleted: sha256:8a32ea11e9d33bb299a15ec9b177902ba7bf91efdbce38f475d516f0f9220c94
    Deleted: sha256:f7c9d3d4ca2f0d6769d51db65f05f5d436c068722c1118fd6cc8a503f9bb818d
    Deleted: sha256:32244df218089a04436d4e2fe44707c174a40820bcc9fdb3535a22c5591e068d
    Deleted: sha256:d3b9c5fb487af1f463183d1239e72ad92219701f08796fcc39b178ab7ac62f41
    Deleted: sha256:c2ebd206bd4165d8fc4a2d7ce4f85ff99d4e5f1580f31b1f5f8997272b989377
    Deleted: sha256:278bac0e795ad7d6adb0426e2931cb7088f66f117c0b70a0a54b0124be641fac
    Deleted: sha256:87d828b7ac5718bbfd772833a41185a6ae88f1564ec8f2394275ac70d92c6d97
    Deleted: sha256:6640581f3917587f423d0aee4a32fd18b5c4b55757ea1241de4a72e366d1b5a2
    Deleted: sha256:b33db874cc4ee42bc5d532a58b11788ac0fa428760092fbf5a05af18c550541e
    Deleted: sha256:c814fc1325860cb847aff0b7bfe97898c60bccba4a4d76a647d673d0998c2e0f
    Deleted: sha256:7f40b9864058d21012dffdf459d81f9190317423554bfc38248aea39fcff0a6f
    Deleted: sha256:bd5e5cb6e0cb6a52756b6c2bf4d3c6e8e6ed07d8466a029979cd3d1c3e577449
    Deleted: sha256:960c459c716dc8fba4f46fa789286fdf5a113daaa0d1bbd1e25f1a3b258c65bb
    Deleted: sha256:67a865d64751c20f9e0901b6d249b4c0df644b40a092020e4f289cee7fa5dd6f
    Deleted: sha256:e0b3aa0887ada860eb2acd760e64e4a6559448dc128dd768c87e6aa93595b3d6
    Deleted: sha256:507746beb268d7b9adc9c63de7edf2dbda0839f960d615ef794113b3e3590103
    Deleted: sha256:9dadb3a1e7525ac4f186ca727f976e9a8a4efb9c1f699ed96a961abfa160cfbc
    Deleted: sha256:9df1be3e9e120fb7dfa528d9b29d84747bec5ec5150899234da53392726b9e2c
    Deleted: sha256:492517438048d114d54594f1db5f4d4df0d1822da633f84fce7690a126e4515d
    Deleted: sha256:c51fc3f0bbecde64db5be9018ab5ab34210ae93d34903d77689468a8abcc78d1
    Deleted: sha256:bf104eb23eaea141a57e7c19d03f5c635c221c9709334640e178f1c71cf9c0ab
    Deleted: sha256:da00cc7b760c48c9efcfc61d435fcb1894cf55c9e0dda00ee67f59d1281cfb91
    Deleted: sha256:bd629c7b68f9e8564ea63afe38a217df7088326c4c47ddbb24d4c107d046f6a9
    Deleted: sha256:bae9026105d2a7d02b61792f958f9342b0855e318235e97e44e2eb1ceadf3878
    Deleted: sha256:d5550781a5b4d4a7392120a58f32caed8909aca415b3dc4d49fd5d5dc1b5f82f
    Deleted: sha256:19aaaefbe1795bbc8caf2d191ce9fefdfe3598e3fdddf8586dc2c40b99c8e2d5
    Deleted: sha256:453599e663126900551bb91a723d5eaa7b0916b3ccea5089895c4e502253f0bb
    Deleted: sha256:d0f94bb7b6c6505377dfd1763b423113d556480e282a21540894bb5844090bb1
    Deleted: sha256:57d990b0ef22c0506cdc889810c54937ee1a372dc0ea1d86d7b56506d89882f8
    Deleted: sha256:b08a6ce9bd29fd603c539c36a771ac6305eae057b9c3a91be80b19216b37094c
    Deleted: sha256:c77460f801823248d76027cddbb14289b88b55f32f783ecda9729de72f803224
    Deleted: sha256:fb95498b848f62c8dd73ab37bf928cf924a1b43fe428cf994af309ad740c9209
    Deleted: sha256:ac22f589229cc93e1ae32ec1996989e63157675bc3ba0560851ae8785898ef1a
    Deleted: sha256:6495897cbe91ef33640c0bb98ffb4860433ae4bfe89be6bcaa2ceb68f691b7d1
    Deleted: sha256:f04a642a8664d07ccf96fa2d57e5464c345eef382b15e75b5d15dc0538d435fa
    Deleted: sha256:881299f8f8726df59cf0b3ee9d3cfe664253ccbb8dde1fffc1dede07c318d4b7
    Deleted: sha256:7af01c297c97fd2230868a56313b65cceaf009f58f6c2c0aba776209656e2bb9
    Untagged: ubuntu:14.04
    Untagged: ubuntu@sha256:62a5dce5ceccd7f1cb2672a571ebee52cad1f08eec9b57fe4965fb0968a9602e
    Deleted: sha256:7c09e61e90350e8f5c0cba2979003bdfe32c2d027b68b4f0cf9063cdd7b4bafd
    Deleted: sha256:304aecb5e13929f85d3ce2e9d83d0212866c8e55a460c94cf24bd75da1c7c153
    Deleted: sha256:f302be18d46a45c0edbbd9b4bc02db764a4b0b8cd9bd0490f33dfaff039a3b62
    Deleted: sha256:c523f3173f6028e5329fd401331c375f7b9b9e831d915fafaf358f55e36e3747
    Deleted: sha256:94e631422130dc414878fd05efe3d59de44c9d8904696a7c299a83f378a92845
    Deleted: sha256:c29b5eadf94a90a2abda13e765d4fad4825fd15621dea1d9a98b60b89b835c2a
    8324f548d9c7
    Error response from daemon: bridge is a pre-defined network and cannot be removed
    Error response from daemon: host is a pre-defined network and cannot be removed
    Error response from daemon: none is a pre-defined network and cannot be removed

**Note:** future releases (i.e. milestone `1.0 <https://github.com/jeff1evesque/machine-learning/milestones/1.0>`_),
will include more granular unit tests, or more logical ordered, such that particular
sets of unit tests will conditionally run upon execution of test dependencies.

It is important to understand that building the corresponding docker containers
needed for the unit tests, is resource intensive, also with respect to the harddisk.
Therefore, the `unit-tests` bash script, properly [cleans-up](https://github.com/jeff1evesque/machine-learning/blob/b9fdb85c55fa99992ed78cba538d5ef7f3c62c64/utility/unit-tests#L75-L89)
after it's execution. Additionally, given that the vagrant development environment,
has not exceeded harddisk limitations, all executions should have necessary space by
default, from an initial `vagrant up xxx`. For example, during the execution of the
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
