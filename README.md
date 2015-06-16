Machine Learning
================

###Definition

Machine learning is a [subfield](http://en.wikipedia.org/wiki/Academic_disciplines) of [computer science](http://en.wikipedia.org/wiki/Computer_science) (CS) and [artificial intelligence](http://en.wikipedia.org/wiki/Artificial_intelligence) (AI) that deals with the construction and study of systems that can [learn](http://en.wikipedia.org/wiki/Learning) from data, rather than follow only explicitly programmed instructions.

- http://en.wikipedia.org/wiki/Machine_learning

Applications for machine learning include:

- [Object recognition](http://en.wikipedia.org/wiki/Object_recognition)
- [Natural language processing](http://en.wikipedia.org/wiki/Natural_language_processing)
- [Search engines](http://en.wikipedia.org/wiki/Search_engines)
- [Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics)
- [Stock market](http://en.wikipedia.org/wiki/Stock_market) analysis
- [Speech](http://en.wikipedia.org/wiki/Speech_recognition) and [handwriting recognition](http://en.wikipedia.org/wiki/Speech_recognition)
- [Sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis)
- [Recommender systems](http://en.wikipedia.org/wiki/Recommender_system)
- [Sequence mining](http://en.wikipedia.org/wiki/Sequence_mining), commonly referred as *data mining*
- [Computational advertising](http://en.wikipedia.org/wiki/Computational_advertising), and [Computational finance](http://en.wikipedia.org/wiki/Computational_finance)

In [machine learning](http://en.wikipedia.org/wiki/Machine_learning), support vector machines (SVMs) are [supervised learning](http://en.wikipedia.org/wiki/Supervised_learning) models with associated learning [algorithms](http://en.wikipedia.org/wiki/Algorithm) that analyze data and recognize patterns, used for [classification](http://en.wikipedia.org/wiki/Statistical_classification) and [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis). 

- http://en.wikipedia.org/wiki/Support_vector_machine

###Overview

##Installation

###Linux Packages

The following packages need to be installed through terminal in Ubuntu:

```
# Gnome UI for Ubuntu:
sudo apt-get install xorg gnome-core gnome-system-tools gnome-app-install

# General Packages:
sudo apt-get install inotify-tools
sudo apt-get install python-pip
sudo pip install redis
sudo pip install jsonschema
sudo pip install xmltodict
sudo pip install six
sudo pip install matplotlib

# Flask with Requests
sudo pip install Flask
sudo pip install requests

# MariaDB with Python Connector:
sudo apt-get install mariadb-server mariadb-client
sudo apt-get install python-mysqldb

# Latest PPA for nodejs:
curl -sL https://deb.nodesource.com/setup | sudo bash -

# Install 'add-apt-repository' command
sudo apt-get install python-software-properties

# Add PPA / install Redis Server
sudo add-apt-repository ppa:rwky/redis
sudo apt-get update
sudo apt-get install redis-server

# ruby / nodejs (includes npm from PPA):
sudo apt-get install ruby
sudo apt-get install nodejs

# Compiler / Minifier:
sudo gem install sass
sudo npm install uglify-js -g
sudo npm install --global imagemin

# Scikit-Learn Dependency:
sudo apt-get build-dep scikit-learn
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system.

**Note:** All MySQL connectors (PHP, Perl, Python, Java, .NET, C, Ruby, etc.) work [unchanged](https://mariadb.com/kb/en/mariadb/faq/mariadb-vs-mysql-compatibility/) with MariaDB.

##Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /[project-directory]
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/machine-learning.git
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /[project-directory]
git remote add upstream https://github.com/[YOUR-USERNAME]/machine-learning.git
```

####GIT Submodule

We need to initialize our git *submodules*:

```
sudo git submodule init
sudo git submodule update
```

The above two commands will update submodules within the cloned repository, according to the versioned master branch. If they are already initialized in the cloned repository, then the latter command will suffice.

The following updates submodule(s):

```
cd /[project-directory]
git checkout -b NEW_BRANCH master
cd [YOUR_SUBMODULE]/
git checkout master
git pull
cd ../
git status
```

to the latest code-base, within the cloned repository branch, `NEW_BRANCH`.

**Note:** the [scikit-learn](https://github.com/scikit-learn/scikit-learn/) submodule can be found in the [`/build/`](https://github.com/jeff1evesque/machine-learning/tree/master/build/) directory.

###Flask

Python's [Flask](http://flask.pocoo.org/), is a microframework based on [Werkzeug](http://werkzeug.pocoo.org/).  Specifically, it is a [web framework](http://en.wikipedia.org/wiki/Web_application_framework), which includes, a development server, integrated support for [unit testing](http://en.wikipedia.org/wiki/Unit_testing), [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) API, and [Jinja2](http://jinja.pocoo.org/) templating.

This project implements flask, by requiring [`app.py`](https://github.com/jeff1evesque/machine-learning/blob/master/app.py) to be running:

```
cd /[project-directory]/machine-learning/
python app.py
```

**Note:** the [`run()`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.run) method within [`app.py`](https://github.com/jeff1evesque/machine-learning/blob/master/app.py), runs the local developement server, and has the ability of defining the host, port, debug feature, and several other options. If none of these attributes are passed into the method, the server will default to running `localhost` on port `5000`, with no [`debug`](http://flask.pocoo.org/docs/0.10/quickstart/#debug-mode) features enabled.

**Note:** when running the above [`app.py`](https://github.com/jeff1evesque/machine-learning/blob/master/app.py), ensure that the terminal window is not used for any other processes, while the web application is available to others.

###Scikit-Learn

[Scikit-Learn](http://scikit-learn.org/stable/) is an open source [machine learning](http://en.wikipedia.org/wiki/Machine_learning) library written in the [Python](http://en.wikipedia.org/wiki/Python_(programming_language)) programming language.  Within this project, *scikit-learn* provides the ability to solve [classification](http://scikit-learn.org/stable/modules/svm.html#classification), and [regression](http://scikit-learn.org/stable/modules/svm.html#regression) problems.

To install the *required* library:

```
cd /[project-directory]/build/scikit-learn/
python setup.py build
sudo python setup.py install
```

###Bash Script

Generally, [bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)) is preferred over [python](http://en.wikipedia.org/wiki/Python_(programming_language)) for simple *file system* oriented tasks. In this repository, bash is used to [*shell script*](http://en.wikipedia.org/wiki/Shell_script) the execution of [sass](http://sass-lang.com/documentation/file.SASS_REFERENCE.html), [uglifyjs](https://www.npmjs.org/package/uglify-js#usage), and [imagemin](https://www.npmjs.org/package/imagemin#usage).

The following command compiles and minifies [javascript](http://en.wikipedia.org/wiki/JavaScript), [css](http://en.wikipedia.org/wiki/Cascading_Style_Sheets), and various [image file formats](http://en.wikipedia.org/wiki/Image_file_formats):

```
cd /[project-directory]/build/
./bash_loader
```

However, the supplied [`app.py`](https://github.com/jeff1evesque/machine-learning/blob/master/app.py) implements the bash script [`bash_loader`](https://github.com/jeff1evesque/machine-learning/blob/master/build/bash_loader) via the [`subprocess`](https://docs.python.org/2/library/subprocess.html) module. Specifically, any commands determined by [`bash_loader`](https://github.com/jeff1evesque/machine-learning/blob/master/build/bash_loader), is automated by the intrinsic RESTful nature of python flask.

**Note:** some of the used [build](https://github.com/jeff1evesque/machine-learning/tree/master/build/web/) scripts, implement [inotifywait](http://linux.die.net/man/1/inotifywait), a linux subkernel responsible for monitoring file system changes.

**Note:** after running [`./bash_loader`](https://github.com/jeff1evesque/machine-learning/blob/master/build/bash_loader) for the first time, it is important to open, and save each file within the [`/src/`](https://github.com/jeff1evesque/machine-learning/tree/master/src) directory.  Otherwise, inotifywait will never detect changes within the respective [`/src/`](https://github.com/jeff1evesque/machine-learning/tree/master/src) files, and never compile the respective files into the [`/web_interface/static/`](https://github.com/jeff1evesque/machine-learning/tree/master/web_interface/static) directory.

###jQuery Validation

[jQuery Validation](http://jqueryvalidation.org/) is a plugin that allows [client-side](http://en.wikipedia.org/wiki/Client-side) validation on [HTML form](http://www.w3.org/TR/html5/forms.html) elements. When a specific field fails validation, a label element is created as the next successive [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) element, indicating the corresponding *error message*.

Additional documentation:

- [jQuery Validation](http://jqueryvalidation.org/documentation/)
- [Validator object](http://jqueryvalidation.org/category/validator/)
- [Validator addMethod](http://jqueryvalidation.org/jQuery.validator.addMethod/)
- [Validation example](http://stackoverflow.com/questions/10843399#answer-10843593)

This project implements client-side validation within [`form_validator.js`](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js). Specific *how-to* can be found within the comments of the javascript [code](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js).

**Note:** this project *may* implement concepts of *machine learning*, where data is not supplied via an HTML form. If data is not supplied by the user (HTML form), then backend-validation (refer to [*JSON Schema*](https://github.com/jeff1evesque/machine-learning#json-schema)) becomes even more crucial.

###JSON Schema

[JSON Schema](https://pypi.python.org/pypi/jsonschema) provides an implementation to validate [JSON](http://en.wikipedia.org/wiki/JSON) data structures. When a specific element within the JSON structure fails validation, an [exception](https://wiki.python.org/moin/HandlingExceptions) is raised indicating the corresponding *error message*.

Additional documentation:

- [Understanding JSON Schema](http://spacetelescope.github.io/understanding-json-schema/)
- [jsonschema](http://python-jsonschema.readthedocs.org/en/latest/)

This project implements JSON Schema validation, as a backend-validation tool. Specifically, modules within the [`/brain/schema/`](https://github.com/jeff1evesque/machine-learning/tree/master/brain/schema) directory, define the schemas, while validation modules in the [`/brain/validator/`](https://github.com/jeff1evesque/machine-learning/tree/master/brain/validator) directory, may implement the respective validation schema(s).

###MariaDB Database

[MariaDB](https://mariadb.org/) is considered an upgrade alternative to [MySQL](http://www.mysql.com/), with [added features](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-features/#extensions-entityampentity-new-features), and [performance enhancements](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-features/#speed-improvements). In general, it is a [drop-in](https://mariadb.com/kb/en/mariadb/faq/mariadb-vs-mysql-compatibility/#mariadb-is-a-binary-drop-in-replacement-for-mysql) replacement for MySQL. Therefore, MariaDB shares identical SQL command syntax, and support for [phpMyAdmin](http://www.phpmyadmin.net/home_page/index.php).

Some interesting features of MariaDB:

- Supports common content management systems (i.e. [Drupal](https://www.drupal.org/), [Wordpress](https://wordpress.com/))
- Can be [implemented](http://www.raspberrypi.org/forums/viewtopic.php?t=12859&p=288820) on the [Raspberry Pi](https://github.com/jeff1evesque/raspberry-pi#definition)

In this project, the default MariaDB database configurations (i.e. host, username, password) can be found in [`db_settings.py`](https://github.com/jeff1evesque/machine-learning/blob/master/brain/database/db_settings.py). Specifically, the `Database` class in `db_settings`, contains methods that allow further customization.

By default, the username `authenticated`, and corresponding password `password` is used to access the SVM database. Therefore, remember to create the corresponding SQL user with sufficient privileges:

```sql
$ mysql -u root -p
MariaDB [(none)]> CREATE USER 'authenticated'@'localhost' IDENTIFIED BY 'password';
MariaDB [(none)]> GRANT CREATE, INSERT, DELETE, UPDATE, DROP, EXECUTE, SELECT, SHOW DATABASES ON *.* TO 'authenticated'@'localhost';
MariaDB [(none)]> FLUSH PRIVILEGES;
```

**Note:** one execution of this program may involve different *dependent*, and *independent* variables then the next execution. Therefore, the database schema is not known ahead of time. For this reason, the [EAV data model](http://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model#Physical_representation_of_EAV_data) is used for storing and retrieving SVM dataset(s).

**Note:** more information regarding the MariaDB syntax, can be found within the Database [wiki page](https://github.com/jeff1evesque/machine-learning/wiki/Database).

###Redis

[Redis](http://redis.io/) is an open source, key-value cache, and store system.  Often classified as [NoSQL](http://en.wikipedia.org/wiki/NoSQL), it is more accurately referred to as, a data structure server.  Though, redis is similar to [Memcached](http://memcached.org/) (some argue faster), in general, it has more features, and greater flexibility.  Some of the more notable advantages of [Redis](http://redis.io/) include:

- Multiple datatypes vs. memcached simple key-value
- Dataset Persistence
- Larger Data Store
- Granular eviction policies

By default, the redis-server autostarts via Ubuntu's [upstart](http://upstart.ubuntu.com/) daemon.  But, it is important the following line from `/etc/init/redis-server.override` is commented out:

```bash
#manual
```

Otherwise, the autostart feature will be overridden, and will require manual start.  Once started, the redis-server will intrinsically implement dataset [snapshotting](http://redis.io/topics/persistence#snapshotting), as defined within [`redis.conf`](https://github.com/antirez/redis/blob/unstable/redis.conf#L170).

**Note:** if needed, the following are basic redis-server commands:

```bash
sudo start redis-server
sudo restart redis-server
sudo stop redis-server
```

**Note:** the term *dataset* refers to the full redis data stored in memory.

This project implements redis, by implementing the [redis-server](https://github.com/antirez/redis), with the [redis-py](https://redis-py.readthedocs.org/en/latest/) client.  Specifically, various python modules in the [`/brain/cache/`](https://github.com/jeff1evesque/machine-learning/tree/master/brain/cache) directory, implements the `Redis_Query` class from [`redis_query.py`](https://github.com/jeff1evesque/machine-learning/blob/master/brain/cache/redis_query.py), using the [redis-py API](https://redis-py.readthedocs.org/en/latest/).

Also, the `start_redis` method, from `redis_query.py` implements a [connection pool](https://pypi.a.ssl.fastly.net/pypi/redis/2.9.1#connection-pools), which allows previous client [connections](https://pypi.a.ssl.fastly.net/pypi/redis/2.9.1#connections) (i.e. idle), to be reused for succesive connections:

```python
pool        = redis.ConnectionPool(host=self.host, port=self.port, db=self.db_num)
self.server = redis.StrictRedis(connection_pool=pool)
```

**Note:** a [connection pool](https://pypi.a.ssl.fastly.net/pypi/redis/2.9.1#connection-pools) manages a set of [connection](https://pypi.a.ssl.fastly.net/pypi/redis/2.9.1#connections) instances. By default, the maximum limit is 10,000 concurrent connections, and can be adjusted within [`redis.conf`](https://github.com/antirez/redis/blob/unstable/redis.conf) ([`maxmemory`](https://github.com/antirez/redis/blob/unstable/redis.conf#L478-L499) directive).

**Note:** more information regarding Redis, can be found within the Redis [wiki page](https://github.com/jeff1evesque/machine-learning/wiki/Redis).

##Testing / Execution


###Web Interface

This project provides a sample [web-interface](https://github.com/jeff1evesque/machine-learning/tree/master/templates/index.html), which supports SVM dataset(s) in csv, or xml format:

- http://localhost:5000/

Specifically, the sample web-interface consists of an HTML5 form, where users supply necessary training, or analysis information. During the training session, users provide csv, or xml file(s) representing the dataset(s). Upon form submission, user supplied form data is validated on the client-side (i.e. javascript, php), converted to a json object (python), validated on the server-side (python), then stored into corresponding EAV database tables (python, mariadb) when necessary.

When using the web-interface, it is important to ensure the csv, or xml file(s) are properly formatted. Dataset(s) poorly formatted will fail to create respective json dataset representation(s). Subsequently, the dataset(s) will not succeed being stored in their correponding database tables.

The following are acceptable syntax:

- [CSV sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/html/machine-learning/data/csv/)
- [XML sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/html/machine-learning/data/xml/)
- [JSON sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/html/machine-learning/data/json/)

**Note:** each dependent variable value (for JSON datasets), is an array (square brackets), since each dependent variable may have multiple observations. 

###Programmatic Interface

When creating (sub)projects of this repository *programmatically*, it is important to leverage existing logic when possible:

- [Dataset validation](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_validator.py)
- [Database methods](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_saver.py)

The same syntax [requirement](https://github.com/jeff1evesque/machine-learning#web-interface) for csv, or xml file(s) to json conversion is required. This means logic contained within [`svm_json.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/svm_json.py) must be implemented if such files are used. However, if using a json object (dataset representation) directly is preferred, then no conversion logic is required. Simply ensure a list of dictionary elements:

```python
{ {'uid': xx, 'title': 'yyy'}, {'svm_dataset': [{'dep_variable_label': 'yyy', 'indep_variable_label': 'yyy', 'indep_variable_value': zz.zz}]}, {'id_entity': xx} }
```

is provided when inserting values into the EAV database tables. Exact syntax can be found in [`data_saver.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_saver.py). Be sure to validate the dataset(s) as needed before storing the dataset(s) in the database.

###Test Scripts
