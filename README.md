# Machine Learning [![Build Status](https://travis-ci.org/jeff1evesque/machine-learning.svg)](https://travis-ci.org/jeff1evesque/machine-learning)

In [machine learning](http://en.wikipedia.org/wiki/Machine_learning), support
vector machines (SVMs) are [supervised learning](http://en.wikipedia.org/wiki/
Supervised_learning) models with associated learning [algorithms](http://en.wi
kipedia.org/wiki/Algorithm) that analyze data and recognize patterns, used for
 [classification](http://en.wikipedia.org/wiki/Statistical_classification) and
 [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis).  More
 generally, machine-learning deals with the construction and study of systems
 that can [learn](http://en.wikipedia.org/wiki/Learning) from data, rather than
 follow only explicitly programmed instructions.

Applications for machine learning include:

- [Object recognition](http://en.wikipedia.org/wiki/Object_recognition)
- [Natural language processing](http://en.wikipedia.org/wiki/Natural_language_processing)
- [Search engines](http://en.wikipedia.org/wiki/Search_engines)
- [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics)
- [Stock market](http://en.wikipedia.org/wiki/Stock_market) analysis
- [Speech](http://en.wikipedia.org/wiki/Speech_recognition) and [handwriting recognition](http://en.wikipedia.org/wiki/Speech_recognition)
- [Sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis)
- [Recommender systems](http://en.wikipedia.org/wiki/Recommender_system)
- [Sequence mining](http://en.wikipedia.org/wiki/Sequence_mining), commonly
 referred as *data mining*
- [Computational advertising](http://en.wikipedia.org/wiki/Computational_advertising)
- [Computational finance](http://en.wikipedia.org/wiki/Computational_finance)

## Support [![paypal](https://camo.githubusercontent.com/11b2f47d7b4af17ef3a803f57c37de3ac82ac039/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f70617970616c2d646f6e6174652d79656c6c6f772e737667)](https://www.paypal.me/jeff1evesque) [![bitcoin](https://camo.githubusercontent.com/c705adb6695b3d8f60b9a005674cb58b3f1ef1cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f6e6174652d626974636f696e2d677265656e2e737667)](http://coinbase.com/jeff1evesque)

Donations are very appreciated.  Smaller donations, could fund a latté, during
 a late night meddling code.  While larger donations, could fund further
 research, by assisting the cost for the following:

- server(s): this could be made open to the public, and implementing machine-
learning.
- peripheral device(s): these device(s) could connect to the machine-learning
 server(s):
  - [raspberry pi](https://www.raspberrypi.org/): these devices could
 communicate to the machine-learning server(s), or *peripheral device(s)*.
  - [xbee chip](www.digi.com/lp/xbee): these chips could implement the
 [zigbee](http://www.zigbee.org/) wireless protocol, allowing peripheral
 device(s) to transmit data between one another, and finally to the machine-
 learning server(s).
  - [sensor](http://www.adafruit.com/categories/35): multiple types of sensors
 could be connected via the [zigbee](http://www.zigbee.org/) wireless protocol
 to other sensor(s), raspberry pi(s), or directly to the machine-learning
 server(s).

## Contributing

Please adhere to [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md)
, when contributing code. Pull requests that deviate from the
 [`contributing.md`](https://github.com/jeff1evesque/machine-learning/blob/master/contributing.md)
, could be [labelled](https://github.com/jeff1evesque/machine-learning/labels)
 as `invalid`, and closed (without merging to master). These best practices
 will ensure integrity, when revisions of code, or issues need to be reviewed.

## Preconfiguration

This project implements puppet's [r10k](https://github.com/puppetlabs/r10k)
 module via vagrant's [plugin](https://github.com/jantman/vagrant-r10k). A
 requirement of this implementation includes a `Puppetfile` (already defined),
 which includes the following syntax:

```ruby
#!/usr/bin/env ruby
## Install Module: stdlib (apt dependency)
mod 'stdlib',
  :git => "git@github.com:puppetlabs/puppetlabs-stdlib.git",
  :ref => "4.6.0"

## Install Module: apt (from master)
mod 'apt',
  :git => "git@github.com:puppetlabs/puppetlabs-apt.git"
...
```

Specifically, this implements the ssh syntax `git@github.com:account/repo.git`,
 unlike the following alternatives:

- `https://github.com/account/repo.git`
- `git://github.com/account/repo.git`

This allows r10k to clone the corresponding puppet module(s), without a
 deterrence of [DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack).
 However, to implement the above syntax, ssh keys need to be generated, and
 properly assigned locally, as well as on the github account.

The following steps through how to implement the ssh keys with respect to
 github:

```bash
$ cd ~/.ssh/
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
Enter passphrase (empty for no passphrase): [Type a passphrase]
Enter same passphrase again: [Type passphrase again]
$ ssh-agent -s
Agent pid 59566
$ ssh-add ~/.ssh/id_rsa
$ pbcopy < ~/.ssh/id_rsa.pub
```

**Note:** it is recommended to simply press enter, to keep default values
 when asked *Enter file in which to save the key*.  Also, if `ssh-agent -s`
 alternative for git bash doesn't work, then `eval $(ssh-agent -s)` for other
 terminal prompts should work.

Then, at the top of any github page (after login), click `Settings > SSH keys >
 Add SSH Keys`, then paste the above copied key into the `Key` field, and click
 *Add key*.  Finally, to test the ssh connection, enter the following within
 the same terminal window used for the above commands:

```bash
$ ssh -T git@github.com
The authenticity of host 'github.com (207.97.227.239)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.252.130' (RSA) to the list of
known hosts.
Hi jeff1evesque! You've successfully authenticated, but GitHub does not provide
shell access.
```

## Configuration

Fork this project in your GitHub account, then clone your repository:

```bash
cd /[PROJECT-DIRECTORY]
sudo git clone https://[USERNAME]@github.com/[USERNAME]/machine-learning.git
```

**Note:** change `[PROJECT-DIRECTORY]` to a desired directory path, and
 `[USERNAME]` to your corresponding git username.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```bash
cd /[PROJECT-DIRECTORY]
git remote add upstream https://github.com/[YOUR-USERNAME]/machine-learning.git
```

## Installation

In order to proceed with the installation for this project, two dependencies
 need to be installed:

- [Vagrant](https://www.vagrantup.com/)
- [Virtualbox](https://www.virtualbox.org/)

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

## Testing / Execution

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

endpoint_url = 'http://localhost:8080/load-data/'
headers = {'Content-Type': 'application/json'}

requests.post(endpoint_url, headers=headers, data=json_string_here)
```

**Note:** the above `post` request, can be implemented in a different language,
 respectively.

The following outlines what the `data` attribute should be, for the above
 `post` implementation:

- [`sample-data-new.json`](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/sample-data-new.json)
- [`sample-data-append.json`](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/sample-data-append.json)
- [`sample-model-generate.json`](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/sample-model-generate.json)
- [`sample-model-predict.json`](https://github.com/jeff1evesque/machine-learning/blob/master/interface/static/data/json/programmatic_interface/sample-model-predict.json)

**Note:** the content of each of the above files, can substituted for the above
 `data` attribute.

#### Data Attributes

The following (non-exhaustive) properties define the above implemented `data`
 attribute:

- `prediction_value[]`: an array of feature values, used to generate a
 corresponding prediction value.  The size of this array, varies depending on
 the number of features that can be expected for the generated model.
- `svm_model_id`: the numeric id value, of the generated model in the nosql
 datastore.
- `svm_model_type`: corresponds to the desired model type, which can be one of
 the following:
  - `classification`
  - `regression`
- `svm_session_id`: the numeric id value, that represents the dataset stored in
 the sql database.
- `svm_session`: corresponds to one of the following session types:
  - `data_new`
  - `data_append`
  - `model_generate`
  - `model_predict`
- `svm_dataset_type` corresponds to one of the following dataset types:
  - `json_string`: indicate that the dataset is being sent via a `post` request

### Test Scripts

This project implements [unit testing](https://en.wikipedia.org/wiki/
Unit_testing), to validate logic in a consistent fashion. Currently, only high-
level unit tests have been defined within [`pytest_session.py`](https://github
.com/jeff1evesque/machine-learning/blob/master/test/programmatic_interface/
pytest_session.py). Future releases (i.e. milestone [1.0](https://github.com/
jeff1evesque/machine-learning/milestones/1.0)), will include more granular unit
 tests. These tests will be automated within a travis [build](https://travis-
ci.org/jeff1evesque/machine-learning), using a docker container, defined within
 the [`Dockerfile`](https://github.com/jeff1evesque/machine-learning/blob/
master/Dockerfile).

Current unit tests cover the following sessions:

- `data_new`
- `data_append`
- `model_predict`
- `model_generate`

which can be executed as follows:

```bash
$ vagrant up
$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-64:~$ pip install pytest
vagrant@vagrant-ubuntu-trusty-64:~$ cd /vagrant/test
vagrant@vagrant-ubuntu-trusty-64:~$ py.test
============================= test session starts ==============================

platform linux2 -- Python 2.7.6, pytest-2.8.0, py-1.4.30, pluggy-0.3.1
rootdir: /vagrant/test, inifile: pytest.ini
collected 4 items

programmatic_interface/pytest_session.py ....

=========================== 4 passed in 1.06 seconds ===========================
```

**Note:** every script within this repository, with the
 [exception](https://github.com/jeff1evesque/machine-learning/issues/2234#issuecomment-158850974)
 of puppet (erb) [templates](https://github.com/jeff1evesque/machine-learning/tree/master/puppet/template),
 and a handful of open source libraries, have been [linted](https://en.wikipedia.org/wiki/Lint_%28software%29)
 via [`.travis.yml`](https://github.com/jeff1evesque/machine-learning/blob/master/.travis.yml).