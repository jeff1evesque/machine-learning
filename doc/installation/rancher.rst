=======
Rancher
=======

The development ecosystem for this application, implements the |rancher|_ orchestration.
This allows various respective docker containers, to be managed in a consistent platform,
where users can properly manage respective services of this application. However, before
proceeding, it is important to follow the docker |installation|_ guide, for the corresponding
host machine.

Once the docker has been installed, execute the following from the docker quickstart terminal,
to install |rancher|_:

.. code:: bash

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
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   622    0   622    0     0   1993      0 --:--:-- --:--:-- --:--:--  2101
    100 3529k  100 3529k    0     0  4434k      0 --:--:-- --:--:-- --:--:-- 4434k
    Archive:  rancher-windows-amd64-v0.6.9.zip
      inflating: rancher.exe

    Windows docker implementation, requires DockerToolbox, which
    creates a 'default' container to manage docker. To proceed,
    rancher configurations will reflect port '8080'.

    21b607e019afd0400ed5e01b63b02b36d0be95e12c26abaf815e332c09f6fd63
    Note: Unnecessary use of -X or --request, POST is already inferred.
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    connect to 192.168.99.100 port 8080 failed: Connection refused
    * Failed to connect to 192.168.99.100 port 8080: Connection refused
    * Closing connection 0
    curl: (7) Failed to connect to 192.168.99.100 port 8080: Connection refused

    Rancher server has not started. Attempting to obtain
    access + secret key, from rancher in 30s.

    Note: Unnecessary use of -X or --request, POST is already inferred.
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    connect to 192.168.99.100 port 8080 failed: Connection refused
    * Failed to connect to 192.168.99.100 port 8080: Connection refused
    * Closing connection 0
    curl: (7) Failed to connect to 192.168.99.100 port 8080: Connection refused

    Rancher server has not started. Attempting to obtain
    access + secret key, from rancher in 30s.

    Note: Unnecessary use of -X or --request, POST is already inferred.
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    connect to 192.168.99.100 port 8080 failed: Connection refused
    * Failed to connect to 192.168.99.100 port 8080: Connection refused
    * Closing connection 0
    curl: (7) Failed to connect to 192.168.99.100 port 8080: Connection refused

    Rancher server has not started. Attempting to obtain
    access + secret key, from rancher in 30s.

    Note: Unnecessary use of -X or --request, POST is already inferred.
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    Connected to 192.168.99.100 (192.168.99.100) port 8080 (#0)
    > POST /v2-beta/apikeys HTTP/1.1
    > Host: 192.168.99.100:8080
    > User-Agent: curl/7.49.1
    > Accept: application/json
    > Content-Type: application/json
    > Content-Length: 272
    >
    } [272 bytes data]
    * upload completely sent off: 272 out of 272 bytes
    100   272    0     0  100   272      0    226  0:00:01  0:00:01 --:--:--   226<
    HTTP/1.1 201 Created
    < Content-Type: application/json; charset=utf-8
    < Date: Tue, 01 May 2018 21:46:34 GMT
    < Expires: Thu, 01 Jan 1970 00:00:00 GMT
    < Server: Jetty(9.2.11.v20150529)
    < Set-Cookie: PL=rancher;Path=/
    < X-Api-Account-Id: 1a1
    < X-Api-Client-Ip: 192.168.99.1
    < X-Api-Schemas: http://192.168.99.100:8080/v2-beta/schemas
    < X-Api-User-Id: 1a1
    < X-Rancher-Version: v1.6.17
    < Content-Length: 1106
    <
    { [1106 bytes data]
    100  1378  100  1106  100   272    492    121  0:00:02  0:00:02 --:--:--   492
    * Connection #0 to host 192.168.99.100 left intact
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
    * Connected to 192.168.99.100 (192.168.99.100) port 8080 (#0)
    > POST /v2-beta/projects/1a5/registrationTokens HTTP/1.1
    > Host: 192.168.99.100:8080
    > User-Agent: curl/7.49.1
    > Accept: application/json
    > Content-Type: application/json
    >
    < HTTP/1.1 201 Created
    < Content-Type: application/json; charset=utf-8
    < Date: Tue, 01 May 2018 21:46:35 GMT
    < Expires: Thu, 01 Jan 1970 00:00:00 GMT
    < Server: Jetty(9.2.11.v20150529)
    < Set-Cookie: PL=rancher;Path=/
    < X-Api-Account-Id: 1a5
    < X-Api-Client-Ip: 192.168.99.1
    < X-Api-Schemas: http://192.168.99.100:8080/v2-beta/projects/1a5/schemas
    < X-Api-User-Id: 1a1
    < X-Rancher-Version: v1.6.17
    < Content-Length: 1168
    <
    {"id":"1c3","type":"registrationToken","links":{"self":"http:\/\/192.168.99.100:
    8080\/v2-beta\/projects\/1a5\/registrationtokens\/1c3","account":"http:\/\/192.1
    68.99.100:8080\/v2-beta\/projects\/1a5\/registrationtokens\/1c3\/account","image
    s":"http:\/\/192.168.99.100:8080\/v2-beta\/projects\/1a5\/registrationtokens\/1c
    3\/images","instances":"http:\/\/192.168.99.100:8080\/v2-beta\/projects\/1a5\/re
    gistrationtokens\/1c3\/instances"},"actions":{"activate":"http:\/\/192.168.99.10
    0:8080\/v2-beta\/projects\/1a5\/registrationtokens\/1c3\/?action=activate","remo
    ve":"http:\/\/192.168.99.100:8080\/v2-beta\/projects\/1a5\/registrationtokens\/1
    c3\/?action=remove","deactivate":"http:\/\/192.168.99.100:8080\/v2-beta\/project
    s\/1a5\/registrationtokens\/1c3\/?action=deactivate"},"baseType":"credential","n
    ame":null,"state":"registering","accountId":"1a5","command":null,"created":"2018
    -05-01T21:46:35Z","createdTS":1525211195000,"description":null,"image":null,"kin
    d":"registrationToken","registrationUrl":null,"removed":null,"token":null,"trans
    itioning":"yes","transitioningMessage":"In Progress","transitioningProgress":nul
    l,"uuid":"1c02f09d-f008-4895-8e67-bf6a550e695d"}* Connection #0 to host 192.168.
    99.100 left intact
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    Connected to 192.168.99.100 (192.168.99.100) port 8080 (#0)
    > GET /v2-beta/projects/1a5/registrationTokens HTTP/1.1
    > Host: 192.168.99.100:8080
    > User-Agent: curl/7.49.1
    > Accept: application/json
    > Content-Type: application/json
    >
    < HTTP/1.1 200 OK
    < Content-Type: application/json; charset=utf-8
    < Date: Tue, 01 May 2018 21:46:35 GMT
    < Expires: Thu, 01 Jan 1970 00:00:00 GMT
    < Server: Jetty(9.2.11.v20150529)
    < Set-Cookie: PL=rancher;Path=/
    < Vary: Accept-Encoding, User-Agent
    < X-Api-Account-Id: 1a5
    < X-Api-Client-Ip: 192.168.99.1
    < X-Api-Schemas: http://192.168.99.100:8080/v2-beta/projects/1a5/schemas
    < X-Api-User-Id: 1a1
    < X-Rancher-Version: v1.6.17
    < Transfer-Encoding: chunked
    <
    { [2476 bytes data]
    100  3526    0  3526    0     0  14160      0 --:--:-- --:--:-- --:--:-- 14160
    * Connection #0 to host 192.168.99.100 left intact
    * timeout on name lookup is not supported
    *   Trying 192.168.99.100...
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*
    Connected to 192.168.99.100 (192.168.99.100) port 8080 (#0)
    > GET /v2-beta/projects/1a5/registrationTokens HTTP/1.1
    > Host: 192.168.99.100:8080
    > User-Agent: curl/7.49.1
    > Accept: application/json
    > Content-Type: application/json
    >
    < HTTP/1.1 200 OK
    < Content-Type: application/json; charset=utf-8
    < Date: Tue, 01 May 2018 21:46:37 GMT
    < Expires: Thu, 01 Jan 1970 00:00:00 GMT
    < Server: Jetty(9.2.11.v20150529)
    < Set-Cookie: PL=rancher;Path=/
    < Vary: Accept-Encoding, User-Agent
    < X-Api-Account-Id: 1a5
    < X-Api-Client-Ip: 192.168.99.1
    < X-Api-Schemas: http://192.168.99.100:8080/v2-beta/projects/1a5/schemas
    < X-Api-User-Id: 1a1
    < X-Rancher-Version: v1.6.17
    < Transfer-Encoding: chunked
    <
    { [3629 bytes data]
    100  3617    0  3617    0     0  32881      0 --:--:-- --:--:-- --:--:-- 38478
    * Connection #0 to host 192.168.99.100 left intact
    Docker machine "rancher" already exists
    export DOCKER_TLS_VERIFY="1"
    export DOCKER_HOST="tcp://192.168.99.101:2376"
    export DOCKER_CERT_PATH="C:\Users\jlevesque\.docker\machine\machines\rancher"
    export DOCKER_MACHINE_NAME="rancher"
    export COMPOSE_CONVERT_WINDOWS_PATHS="true"
    # Run this command to configure your shell:
    # eval $("C:\Program Files\Docker Toolbox\docker-machine.exe" env rancher)

    INFO: Running Agent Registration Process, CATTLE_URL=http://192.168.99.100:8080/
    v1
    INFO: Attempting to connect to: http://192.168.99.100:8080/v1
    INFO: http://192.168.99.100:8080/v1 is accessible
    INFO: Inspecting host capabilities
    INFO: Boot2Docker: true
    INFO: Host writable: false
    INFO: Token: xxxxxxxx
    INFO: Running registration
    INFO: Printing Environment
    INFO: ENV: CATTLE_ACCESS_KEY=50FA9C91251B3B689717
    INFO: ENV: CATTLE_HOME=/var/lib/cattle
    INFO: ENV: CATTLE_REGISTRATION_ACCESS_KEY=registrationToken
    INFO: ENV: CATTLE_REGISTRATION_SECRET_KEY=xxxxxxx
    INFO: ENV: CATTLE_SECRET_KEY=xxxxxxx
    INFO: ENV: CATTLE_URL=http://192.168.99.100:8080/v1
    INFO: ENV: DETECTED_CATTLE_AGENT_IP=192.168.99.101
    INFO: ENV: RANCHER_AGENT_IMAGE=rancher/agent:stable
    INFO: Deleting container rancher-agent
    INFO: Launched Rancher Agent: 8f944921e3462dcf98f4b0a9339d9aa7f35a3751750305ba1e
    f0105c2a58b71f
    1st5

**Note:** when starting the docker terminal, make sure to `Run as administrator`.

Once the rancher build succeeds, a single `MLStack` will be created:

.. image:: https://user-images.githubusercontent.com/2907085/39613056-9cf9289e-4f32-11e8-97ac-608c4bd21672.JPG

This stack will contain numerous services, each assigned to it's respective container:

.. image:: https://user-images.githubusercontent.com/2907085/39613057-9d06f0aa-4f32-11e8-8fe4-5a9d58d387dd.JPG

Each can be individually inspected. However, the actual application can be accessed:

.. image:: https://user-images.githubusercontent.com/2907085/39499223-97b96fce-4d7a-11e8-96e2-c4e31f6b8e09.JPG

.. |rancher| replace:: rancher
.. _rancher: http://rancher.com

.. |installation| replace:: installation
.. _installation: docker
