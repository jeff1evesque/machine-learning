==========
Puppetfile
==========

This project implements puppet's |r10k|_ module via vagrant's `plugin <https://github.com/jantman/vagrant-r10k>`_.
A requirement of this implementation includes a ``Puppetfile`` (already defined),
which includes the following syntax:

.. code:: ruby

    #!/usr/bin/env ruby
    ## Install Module: stdlib (apt dependency)
    mod 'stdlib',
      :git => "git@github.com:puppetlabs/puppetlabs-stdlib.git",
      :ref => "4.6.0"

    ## Install Module: apt (from master)
    mod 'apt',
      :git => "git@github.com:puppetlabs/puppetlabs-apt.git"
    ...

Specifically, this implements the ssh syntax ``git@github.com:account/repo.git``,
unlike the following alternatives:

- ``https://github.com/account/repo.git``
- ``git://github.com/account/repo.git``

This allows r10k to clone the corresponding puppet module(s), without a deterrence
of |DDoS|_. However, to implement the above syntax, ssh keys need to be generated,
and properly assigned locally, as well as on the github account.

.. |r10k| replace:: ``r10k``
.. _r10k: https://github.com/puppetlabs/r10k
.. |DDoS| replace:: ``DDoS``
.. _DDoS: https://en.wikipedia.org/wiki/Denial-of-service_attack
