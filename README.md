# Machine Learning [![Build Status](https://travis-ci.org/jeff1evesque/machine-learning.svg?branch=master)](https://travis-ci.org/jeff1evesque/machine-learning) [![Coverage Status](https://coveralls.io/repos/github/jeff1evesque/machine-learning/badge.svg?branch=master)](https://coveralls.io/github/jeff1evesque/machine-learning?branch=master)

This project provides a [web-interface](https://github.com/jeff1evesque/machine-learning/blob/master/README.md#web-interface),
 as well as a [programmatic-api](https://github.com/jeff1evesque/machine-learning/blob/master/README.md#programmatic-interface)
 for various machine learning algorithms. Some of it's general applications, have
 been outlined within [`index.rst`](https://github.com/jeff1evesque/machine-learning/blob/master/doc/index.rst).

**Supported algorithms**:

- [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) (SVM)
- [Support Vector Regression](https://en.wikipedia.org/wiki/Support_vector_machine#Regression) (SVR)

## Contributing

Please adhere to [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md),
 when contributing code. Pull requests that deviate from the
 [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md),
 could be [labelled](https://github.com/jeff1evesque/machine-learning/labels)
 as `invalid`, and closed (without merging to master). These best practices
 will ensure integrity, when revisions of code, or issues need to be reviewed.

**Note:** support, and philantropy can be [inquired](https://github.com/jeff1evesque/machine-learning/blob/master/doc/contribution/support.rst),
 to further assist with development.

## Configuration

Fork this project, and remember to [generate](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/ssh_keys.rst)
 ssh keys, before cloning the repository:

- [simple clone](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#simple-clone):
 clone the remote master branch.
- [commit hash](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#commit-hash):
 clone the remote master branch, then checkout a specific commit hash.
- [release tag](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#release-tag):
 clone the remote branch, associated with the desired release tag.

**Note:** the [`puppetfile.rst`](https://github.com/jeff1evesque/machine-learning/blob/master/doc/background/puppetfile.rst)
 can be reviewed, to better understand why ssh keys are required.

## Installation

In order to proceed with the installation for this project, docker must be installed:

### Legacy: Windows
- [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/): allows Docker use on systems
that do not meet [Docker for Windows](https://docs.docker.com/docker-for-windows/) minimal system requirements.

### Community Edition
- [windows](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows)
- [ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [centos](https://docs.docker.com/install/linux/docker-ce/centos/)
- [mac](https://docs.docker.com/docker-for-mac/install/)

**Note:** if the host machine is windows, then [cygwin](https://www.cygwin.com/) will need to
be installed, in order for the `make build` command to succeed installing `rancher-compose`.

Once the necessary dependencies have been installed, execute the following
within the docker quickstart terminal, to install [rancher](https://rancher.com/):

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

The following lines, from our `docker-compose.development.yml` indicate corresponding port forwards:

```bash
...
    ports:
      - "5000:8080"
      - "6000:9090"
...
```

**Note:** ssl is configured on the [reverse proxy](https://www.nginx.com/resources/admin-guide/reverse-proxy/),
 such that accessing `http://localhost:8080`, on the host machine, will redirect to `https://localhost:8080`.

## Execution

Both the web-interface, and the programmatic-api, have corresponding
 [unit tests](https://github.com/jeff1evesque/machine-learning/blob/master/doc/test/pytest.rst)
 which can be reviewed, and implemented.

### Web Interface

The [web-interface](https://github.com/jeff1evesque/machine-learning/blob/master/interface/templates/index.html),
 or GUI implementation, allow users to implement the following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
- `data_new`, or `data_append` session), generate a corresponding model into
- `model_predict`: using a previous stored model (from an earlier
 `model_predict` session), from the implemented nosql datastore, along with
 user supplied values, generate a corresponding prediction.

When using the web-interface, it is important to ensure the csv, xml, or json
 file(s), representing the corresponding dataset(s), are properly formatted.
 Dataset(s) poorly formatted will fail to create respective json dataset
 representation(s). Subsequently, the dataset(s) will not succeed being stored
 into corresponding database tables; therefore, no model, or prediction can be
 made.

The following are acceptable syntax:

- [CSV sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/csv/)
- [XML sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/xml/)
- [JSON sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/interface/static/data/json/web_interface)

**Note:** each dependent variable value (for JSON datasets), is an array
 (square brackets), since each dependent variable may have multiple
 observations.

As mentioned earlier, the web application can be accessed after subsequent
 `vagrant up` command, followed by using a browser referencing localhost:8080,
 on the host machine.

### Programmatic Interface

The programmatic-interface, or set of API, allow users to implement the
 following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
- `data_new`, or `data_append` session), generate a corresponding model into
- `model_predict`: using a previous stored model (from an earlier
 `model_predict` session), from the implemented nosql datastore, along with
 user supplied values, generate a corresponding prediction.

A post request, can be implemented in python, as follows:

```python
import requests

endpoint = 'https://localhost:9090/load-data'
headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
}

requests.post(endpoint, headers=headers, data=json_string_here)
```

**Note:** more information, regarding how to obtain a valid `token`, can be further
 reviewed, in the `/login` [documentation](https://github.com/jeff1evesque/machine-learning/tree/master/doc/programmatic_interface/authentication/login.rst).

**Note:** various `data` [attributes](https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic_interface/data_attributes.rst) can be nested in above `POST` request.

It is important to remember that the [`Vagrantfile`](https://github.com/jeff1evesque/machine-learning/blob/98c7f57986cbe56ca14f8ee47859b50a08c2ef9b/Vagrantfile#L54-L55),
 as denoted by the above snippet, has defined two port forwards. Specifically, on
 the host, `8080` is reserved for the web-interface, while `9090`, is reserved for
 the programmatic rest-api.
