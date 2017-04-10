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

Fork this project to your GitHub account. Then, remember to [generate](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/ssh_keys.rst)
 ssh keys, followed by cloning your repository, with one of the following approaches:

- [simple clone](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#simple-clone):
 clone the remote master branch.
- [commit hash](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#commit-hash):
 clone the remote master branch, then checkout a specific commit hash.
- [release tag](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#release-tag):
 clone the remote branch, associated with the desired release tag.

**Note:** the [`puppetfile.rst`](https://github.com/jeff1evesque/machine-learning/blob/master/doc/background/puppetfile.rst)
 can be reviewed, to better understand why ssh keys are required.

## Installation

In order to proceed with the installation for this project, two dependencies
 need to be installed:

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/) (with extension pack)

Once the necessary dependencies have been installed, execute the following
 command to build the virtual environment:

```bash
cd /path/to/machine-learning/
vagrant up
```

Depending on the network speed, the build can take between 10-15 minutes. So,
 grab a cup of coffee, and perhaps enjoy a danish while the virtual machine
 builds. Remember, the application is intended to run on localhost, where the
 [`Vagrantfile`](https://github.com/jeff1evesque/machine-learning/blob/master/Vagrantfile)
 defines the exact port-forward on the host machine.

**Note:** a more complete refresher on virtualization, can be found within the
 vagrant [wiki page](https://github.com/jeff1evesque/machine-learning/wiki/Vagrant).

The following lines, indicate the application is accessible via
 `localhost:8080`, on the host machine:

```bash
...
  ## Create a forwarded port mapping which allows access to a specific port
  #  within the machine from a port on the host machine. In the example below,
  #  accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  config.vm.network "forwarded_port", guest: 443, host: 8585
...
```

Otherwise, if ssl is configured, then the application is accessible via
 `https://localhost:8585`, on the host machine.

**Note:** general convention implements port `443` for ssl.

## Execution

Both the web-interface, and the programmatic-api, have corresponding
 [unit tests](https://github.com/jeff1evesque/machine-learning/blob/master/doc/unit_test/pytest.rst)
 which can be reviewed, and implemented.

### Web Interface

The [web-interface](https://github.com/jeff1evesque/machine-learning/blob/master/interface/templates/index.html)
, or GUI implementation, allow users to implement the following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
 `data_new`, or `data_append` session), generate a corresponding model into the
 implemented nosql datastore.
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
 `vagrant up` command, followed by using a browser referencing localhost:8080
 (or [https://localhost:5050](https://localhost:5050), with ssl), on the host
 machine.

### Programmatic Interface

The programmatic-interface, or set of API, allow users to implement the
 following sessions:

- `data_new`: store the provided dataset(s), within the implemented sql
 database.
- `data_append`: append additional dataset(s), to an existing representation
 (from an earlier `data_new` session), within the implemented sql database.
- `model_generate`: using previous stored dataset(s) (from an earlier
 `data_new`, or `data_append` session), generate a corresponding model into
 the implemented nosql datastore.
- `model_predict`: using a previous stored model (from an earlier
 `model_predict` session), from the implemented nosql datastore, along with
 user supplied values, generate a corresponding prediction.

A post request, can be implemented in python, as follows:

```python
import requests

endpoint_url = 'http://localhost:8080/load-data'
headers = {'Content-Type': 'application/json'}

requests.post(endpoint_url, headers=headers, data=json_string_here)
```

**Note:** the above `post` request, can be implemented in a different language,
 respectively.

**Note:** various `data` [attributes](https://github.com/jeff1evesque/machine-learning/doc/programmatic_interface/data_attributes.rst) can be nested in above `POST` request.
