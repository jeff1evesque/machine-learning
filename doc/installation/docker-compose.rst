==============
Docker Compose
==============

The development ecosystem for this application, can be run via |docker-compose|_.
This allows various respective docker containers, to be managed consistently.
However, before proceeding, it is important to follow the |docker|_ , and
|docker-compose|_ installation guide.

Once docker-compose has installed, simply run ``docker-compose up``, in the
root directory of this cloned project. This will allow the web-application to
be accessible on the host machine, via https://localhost:8080. Similarly, the
programmatic-api will be accessible at https://localhost:9090.

.. |docker-compose| replace:: docker-compose
.. _docker-compose: https://docs.docker.com/compose/install/#install-compose

.. |docker| replace:: docker
.. _docker: https://docs.docker.com/install/