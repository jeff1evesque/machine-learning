==============
Docker Compose
==============

The development ecosystem for this application, can be run via |docker-compose|_.
This allows various respective docker containers, to be managed consistently.
However, before proceeding, it is important to follow the |docker|_ , and
|docker-compose|_ installation guide.

Once docker-compose has installed, simply run ``docker-compose up``:

.. code:: bash

    cd /path/to/machine-learning
    docker-compose up

This will allow the web-application to
be accessible on the host machine, via https://localhost:8080. Similarly, the
programmatic-api will be accessible at https://localhost:9090. However, since
this project assumes rancher as the primary method to deploy, and run the
application, it will be important to remember when reading through this
documentation, to substitute the localhost, or the `https://127.0.0.1:XXXX`
address, in place of the `https://192.168.99.101:XXXX` endpoint. This will
allow users to perform the same tasks outlined throughout this documentation.

.. |docker-compose| replace:: docker-compose
.. _docker-compose: https://docs.docker.com/compose/install/#install-compose

.. |docker| replace:: docker
.. _docker: https://docs.docker.com/install/