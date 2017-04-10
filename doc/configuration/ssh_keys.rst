========
SSH Keys
========

The following steps through how to generate ssh keys with respect to github:

.. code:: bash

    $ cd ~/.ssh/
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
    Enter passphrase (empty for no passphrase): [Type a passphrase]
    Enter same passphrase again: [Type passphrase again]
    $ ssh-agent -s
    Agent pid 59566
    $ ssh-add ~/.ssh/id_rsa
    $ pbcopy < ~/.ssh/id_rsa.pub

**Note:** it is recommended to simply press enter, to keep default values
when asked *Enter file in which to save the key*.  Also, if ``ssh-agent -s``
alternative for git bash doesn't work, then ``eval $(ssh-agent -s)`` for
other terminal prompts should work.

Then, at the top of any github page (after login), click ``Settings > SSH keys >
Add SSH Keys``, then paste the above copied key into the ``Key`` field, and click
*Add key*.  Finally, to test the ssh connection, enter the following within
the same terminal window used for the above commands:

.. code:: bash

    $ ssh -T git@github.com
    The authenticity of host 'github.com (207.97.227.239)' can't be established.
    RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'github.com,192.30.252.130' (RSA) to the list of
    known hosts.
    Hi jeff1evesque! You've successfully authenticated, but GitHub does not provide
    shell access.
