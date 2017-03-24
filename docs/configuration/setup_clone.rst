============
Simple clone
============

.. code:: bash

    cd /[destination-directory]
    sudo git clone https://[account]@github.com/[account]/machine-learning.git
    cd machine-learning
    git remote add upstream https://github.com/[account]/machine-learning.git

**Note:** ``[destination-directory]`` corresponds to the desired
directory path, where the project repository resides. ``[account]``
corresponds to the git username, where the repository is being cloned
from. If the original repository was forked, then use your git username,
otherwise, use ``jeff1evesque``.

===========
Commit hash
===========

.. code:: bash

    cd /[destination-directory]
    sudo git clone https://[account]@github.com/[account]/machine-learning.git
    cd machine-learning
    git remote add upstream https://github.com/[account]/machine-learning.git
    # stop vagrant
    vagrant halt
    # ensure diffs don't prevent checkout, then checkout hash
    git checkout -- .
    git checkout [hash]

**Note:** the hashes associated with a release, can be found under the
corresponding tag value, on the
`release page
<http://www.github.com/jeff1evesque/machine-learning/releases>`_.


**Note:** ``[destination-directory]`` corresponds to the desired
directory path, where the project repository resides. ``[account]``
corresponds to the git username, where the repository is being cloned
from. If the original repository was forked, then use your git username,
otherwise, use ``jeff1evesque``.

===========
Release tag
===========

.. code:: bash

    cd /[destination-directory]
    # clone release tag: master branch does not exist
    sudo git clone -b [release-tag] --single-branch --depth 1 https://github.com/[account]/machine-learning.git [destination-directory]
    git remote add upstream https://github.com/[account]/machine-learning.git
    # create master branch from remote master
    cd machine-learning
    git checkout -b master
    git pull upstream master
    # return to release tag branch
    git checkout [release-tag]

**Note:** ``[release-tag]`` corresponds to the `release
tag <https://github.com/jeff1evesque/machine-learning/tags>`_ value,
used to distinguish between releases.

**Note:** ``[destination-directory]`` corresponds to the desired
directory path, where the project repository resides. ``[account]``
corresponds to the git username, where the repository is being cloned
from. If the original repository was forked, then use your git username,
otherwise, use ``jeff1evesque``.
