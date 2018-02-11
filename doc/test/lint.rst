====
Lint
====

This project provides the ability to lint various language syntax, across the
entire project:

- |flake8|_
- |scss_lint|_
- |bootlint|_
- |puppet|_: as ``puppet parser validate``
- |puppet-lint|_
- |r10k|_: as ``r10k puppetfile check Puppetfile``
- |jsonlint|_
- |csvlint|_
- |xmllint|_
- |mdl|_
- |shellcheck|_
- |yaml-lint|_
- |dockerlint|_
- |rstlint|_

Specifically, anytime code is introduced to the repository, whether through
``git commit``, or some variation of ``git merge``, our |.travis.yml|_
will immediately start the |linter|_. However, the ``linter`` can also be
run manually, after the above depedencies have been installed

.. code:: bash

    cd /vagrant/test
    ./linter install

Then, linting can be executed:

.. code:: bash

    cd /vagrant/test
    ./linter run /vagrant

**Note:** the second argument ``/vagrant``, defines an acceptable current
working directory.

**Note:** custom `configs <https://github.com/jeff1evesque/machine-learning/tree/master/test/lint>`_,
allow more customtomized rules, for the above implemented linters.

.. |flake8| replace:: ``flake8``
.. _flake8: http://flake8.pycqa.org

.. |scss_lint| replace:: ``scss_lint``
.. _scss_lint: https://github.com/brigade/scss-lint/blob/master/lib/scss_lint/linter/README.md

.. |bootlint| replace:: ``bootlint``
.. _bootlint: https://github.com/twbs/bootlint

.. |puppet| replace:: ``puppet``
.. _puppet: https://docs.puppet.com/puppet/4.5/man/parser.html#EXAMPLES

.. |puppet-lint| replace:: ``puppet-lint``
.. _puppet-lint: http://puppet-lint.com/

.. |r10k| replace:: ``r10k``
.. _r10k: /latest/html/test/pytest

.. |jsonlint| replace:: ``jsonlint``
.. _jsonlint: https://github.com/zaach/jsonlint/blob/master/README.md

.. |csvlint| replace:: ``csvlint``
.. _csvlint: https://github.com/theodi/csvlint.rb/blob/master/README.md

.. |xmllint| replace:: ``xmllint``
.. _xmllint: http://xmlsoft.org/xmllint.html

.. |mdl| replace:: ``mdl``
.. _mdl: https://github.com/markdownlint/markdownlint/blob/master/README.md

.. |shellcheck| replace:: ``shellcheck``
.. _shellcheck: https://github.com/koalaman/shellcheck/blob/master/README.md

.. |yaml-lint| replace:: ``yaml-lint``
.. _yaml-lint: https://github.com/Pryz/yaml-lint/blob/master/README.md

.. |dockerlint| replace:: ``dockerlint``
.. _dockerlint: https://github.com/RedCoolBeans/dockerlint/blob/master/README.md

.. |rstlint| replace:: ``rstlint``
.. _rstlint: https://github.com/twolfson/restructuredtext-lint/blob/master/README.rst

.. |.travis.yml| replace:: ``.travis.yml``
.. _.travis.yml: https://github.com/jeff1evesque/machine-learning/blob/e6556b231c6bba38da0a28e5391c1508fea4d64f/.travis.yml

.. |linter| replace:: ``linter``
.. _linter: https://github.com/jeff1evesque/machine-learning/blob/05fcd7a0a81976c37998507148a0a9ff13fce462/test/linter
