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

Fork this project, using of the following methods:

- [simple clone](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#simple-clone):
 clone the remote master branch.
- [commit hash](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#commit-hash):
 clone the remote master branch, then checkout a specific commit hash.
- [release tag](https://github.com/jeff1evesque/machine-learning/blob/master/doc/configuration/setup_clone.rst#release-tag):
 clone the remote branch, associated with the desired release tag.

## Installation

To proceed with the installation for this project, both docker and rancher must be
installed. Installing docker must be done manually, to fulfill a set of [dependencies](https://jeff1evesque.github.io/machine-learning.docs/latest/html/installation/dependencies).
Once completed, rancher can be installed, and automatically configured, by simply
executing a provided bash script, from the docker quickstart terminal:

```bash
cd /path/to/machine-learning
./install-rancher
```

**Note:** the installation, and the configuration of rancher, has been [outlined](https://jeff1evesque.github.io/machine-learning.docs/latest/html/installation/rancher)
if more explicit instructions are needed.

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
