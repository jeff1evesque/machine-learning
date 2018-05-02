=======
Rancher
=======

The development ecosystem for this application, implements the |rancher|_ orchestration.
This allows various respective docker containers, to be managed in a consistent platform,
where users can properly manage respective services of this application. However, before
proceeding, it is important to follow the docker |installation|_ guide, for the corresponding
host machine.

Once the docker has been installed, execute the following from the docker quickstart terminal,
to install [rancher](https://rancher.com/):

```bash



                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/

docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com

Start interactive shell

jeff1evesque@XXXXXXX YYYYYZZ ~
$ cd /path/to/machine-learning

jeff1evesque@XXXXXXX YYYYYZZ /path/to/machine-learning (feature-2935)
$ ./install_rancher
Unable to find image 'rancher/server:latest' locally
latest: Pulling from rancher/server
bae382666908: Pull complete
29ede3c02ff2: Pull complete
da4e69f33106: Pull complete
8d43e5f5d27f: Pull complete
b0de1abb17d6: Pull complete
422f47db4517: Pull complete
79d37de643ce: Pull complete
69d13e08a4fe: Pull complete
2ddfd3c6a2b7: Pull complete
bc433fed3823: Pull complete
b82e188df556: Pull complete
dae2802428a4: Pull complete
a6247572ea3c: Pull complete
884c916ebae4: Pull complete
85517c9c5365: Pull complete
02dded9fe690: Pull complete
fd9f433c3bc6: Pull complete
44d91b3fea45: Pull complete
0d463387dfeb: Pull complete
60753c4d26f0: Pull complete
a003892966fe: Pull complete
Digest: sha256:42441f0128fae4d72d51f92de2049392427d462356282a46f28434332967c7e4
Status: Downloaded newer image for rancher/server:latest
57e7f8577c7a80d8ea10d1b0855de619c4ec9ad0318172b1f52e70006b99afa6
```

**Note:** when starting the docker terminal, make sure to `Run as administrator`.

The following |docker-compose.development.yml|_ lines indicate corresponding port forward:

.. code:: bash

    ports:
      - "5000:8080"
      - "6000:9090"

.. |rancher| replace:: rancher
.. _rancher: http://rancher.com

.. |installation| replace:: installation
.. _installation: docker

.. |docker-compose.development.yml| replace:: ``docker-compose.development.yml``
.. _docker-compose.development.yml: https://github.com/jeff1evesque/machine-learning/blob/master/docker-compose.development.yml