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
sudo pip install jsonschema
sudo pip install python-magic

# LAMP (with MariaDB, and phpmyadmin):
sudo apt-get install apache2
sudo apt-get install mariadb-server mariadb-client
sudo apt-get install php5 libapache2-mod-php5
sudo apt-get install phpmyadmin

# Python to MariaDB / MySQL Connector:
sudo apt-get install python-mysqldb

# Latest PPA for nodejs:
curl -sL https://deb.nodesource.com/setup | sudo bash -

# ruby / nodejs (includes npm from PPA):
sudo apt-get install ruby
sudo apt-get install nodejs

# Compiler / Minifier:
sudo gem install sass
sudo npm install uglify-js -g
sudo npm install --global imagemin

# Scikit-Learn Dependency:
sudo apt-get install python-numpy
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system.

**Note:** All MySQL connectors (PHP, Perl, Python, Java, .NET, C, Ruby, etc.) work [unchanged](https://mariadb.com/kb/en/mariadb/faq/mariadb-vs-mysql-compatibility/) with MariaDB.

##Configuration

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/
sudo mv www/ _www/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/machine-learning.git www
```

Then, change the *file permissions* for the entire project by issuing the command:

```
cd /var/
sudo chown -R jeffrey:sudo www
```

**Note:** change 'jeffrey' to the user account YOU use.

Then, add the *Remote Upstream*, this way we can pull any merged pull-requests:

```
cd /var/www/
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
cd /var/www/
git checkout -b NEW_BRANCH master
cd [YOUR_SUBMODULE]/
git checkout master
git pull
cd ../
git status
```

to the latest code-base, within the cloned repository branch, `NEW_BRANCH`.

###Scikit-Learn

[Scikit-Learn](http://scikit-learn.org/stable/) is an open source [machine learning](http://en.wikipedia.org/wiki/Machine_learning) library written in the [Python](http://en.wikipedia.org/wiki/Python_(programming_language)) programming language.  Within this project, *scikit-learn* provides the ability to solve [classification](http://scikit-learn.org/stable/modules/svm.html#classification), and [regression](http://scikit-learn.org/stable/modules/svm.html#regression) problems.

This repository requires *Scikit-Learn*:

```
cd /var/www/library/scikit-learn/
python setup.py build
sudo python setup.py install
```

###Bash Script

Generally, [bash](http://en.wikipedia.org/wiki/Bash_(Unix_shell)) is preferred over [python](http://en.wikipedia.org/wiki/Python_(programming_language)) for simple *file system* oriented tasks. In this repository, bash is used to [*shell script*](http://en.wikipedia.org/wiki/Shell_script) the execution of [sass](http://sass-lang.com/documentation/file.SASS_REFERENCE.html), [uglifyjs](https://www.npmjs.org/package/uglify-js#usage), and [imagemin](https://www.npmjs.org/package/imagemin#usage).

The following command compiles and minifies [javascript](http://en.wikipedia.org/wiki/JavaScript), [css](http://en.wikipedia.org/wiki/Cascading_Style_Sheets), and various [image file formats](http://en.wikipedia.org/wiki/Image_file_formats):

```
cd /var/www/bash/
./bash_loader
```

Alternatively, configuring `/etc/rc.local` allows bash-scripts to be run during [apache2](https://help.ubuntu.com/10.04/serverguide/httpd.html) boot:

```
...
# run 'bash_loader' at start-up for 'machine-learning' application (edited by JL)
cd /var/www/bash/ && ./bash_loader > /dev/null 2>&1 &

exit 0
```

Since some [build](https://github.com/jeff1evesque/machine-learning/tree/master/bash/build/) scripts implement [*inotifywait*](http://linux.die.net/man/1/inotifywait), a linux subkernel that monitors file system changes, the above changes would allow each respective *build* script to be automated.

**Note:** The above configuration may require [rc.local](http://www.linux.com/news/enterprise/systems-management/8116-an-introduction-to-services-runlevels-and-rcd-scripts) to be *(re)started*:

```
sudo /etc/init.d/rc.local start
```

###jQuery Validation

[jQuery Validation](http://jqueryvalidation.org/) is a plugin that allows [client-side](http://en.wikipedia.org/wiki/Client-side) validation on [HTML form](http://www.w3.org/TR/html5/forms.html) elements. When a specific field fails validation, a label element is created as the next successive [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) element, indicating the corresponding *error message*.

The following provides additional documentation on the jQuery plugin:

- http://jqueryvalidation.org/documentation/
- http://jqueryvalidation.org/category/validator/
- http://jqueryvalidation.org/jQuery.validator.addMethod/
- http://stackoverflow.com/questions/10843399#answer-10843593

This project implements client-side validation within [`form_validator.js`](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js). Specific *how-to* can be found within the comments of the javascript [code](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js).

**Note:** this project *may* implement concepts of *machine learning*, where data is not supplied via an HTML form. If data is not supplied by the user (HTML form), then backend-validation (refer to [*JSON Schema*](https://github.com/jeff1evesque/machine-learning#json-schema)) becomes even more crucial.

###JSON Schema

[JSON Schema](https://pypi.python.org/pypi/jsonschema) provides an implementation to validate [JSON](http://en.wikipedia.org/wiki/JSON) data structures. When a specific element within the JSON structure fails validation, an [exception](https://wiki.python.org/moin/HandlingExceptions) is raised indicating the corresponding *error message*.

The following provides additional documentation on the *schema* validation:

- http://spacetelescope.github.io/understanding-json-schema/
- http://python-jsonschema.readthedocs.org/en/latest/

This project implements *JSON Schema* validation, as a backend-validation tool. Specifically, [`config.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/config.py) defines acceptable *schemas* to validate against, while [`data_validator.py`](https://github.com/jeff1evesque/machine-learning/blob/52157d2f7c7255f999e822dd13ce65911d678918/python/data_validator.py#L48) implements the validation schema(s).

###MariaDB Database

[MariaDB](https://mariadb.org/) is considered an upgrade alternative to [MySQL](http://www.mysql.com/), with [added features](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-features/#extensions-entityampentity-new-features), and [performance enhancements](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-features/#speed-improvements). In general, it is a [drop-in](https://mariadb.com/kb/en/mariadb/faq/mariadb-vs-mysql-compatibility/#mariadb-is-a-binary-drop-in-replacement-for-mysql) replacement for MySQL. Therefore, MariaDB shares identical SQL command syntax, and support for [phpMyAdmin](http://www.phpmyadmin.net/home_page/index.php).

Some interesting features of MariaDB:

- Supports common content management systems (i.e. [Drupal](https://www.drupal.org/), [Wordpress](https://wordpress.com/))
- Can be [implemented](http://www.raspberrypi.org/forums/viewtopic.php?t=12859&p=288820) on the [Raspberry Pi](https://github.com/jeff1evesque/raspberry-pi#definition)

In this project, the default MariaDB database configurations (i.e. host, username, password) can be found in [`config.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/config.py). Specifically, the `Database` class in `config.py`, contains methods that allow further customization.

By default, the username `authenticated`, and corresponding password `password` is used to access the SVM database. Therefore, remember to create the corresponding SQL user with sufficient privileges:

```sql
$ mysql -u root -p
MariaDB [(none)]> CREATE USER 'authenticated'@'localhost' IDENTIFIED BY 'password';
MariaDB [(none)]> GRANT CREATE, INSERT, DELETE, DROP, EXECUTE, SELECT, SHOW DATABASES ON *.* TO 'authenticated'@'localhost';
MariaDB [(none)]> FLUSH PRIVILEGES;
```

**Note:** more information regarding the MariaDB syntax can be found within the [Database](https://github.com/jeff1evesque/machine-learning/wiki/Database) wiki.

**Note:** one execution of this program may involve different *dependent*, and *independent* variables then the next execution. Therefore, the database schema is not known ahead of time. For this reason, the [EAV data model](http://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model#Physical_representation_of_EAV_data) is used for storing and retrieving SVM dataset(s).

##Testing / Execution


###Web Interface

This project provides a sample [web-interface](https://github.com/jeff1evesque/machine-learning/blob/master/html/machine-learning/test/php/index.php):

- http://localhost/machine-learning/test/php/

which supports SVM dataset(s) in csv, or xml format. Upon dataset submission (i.e. training), the data is validated on the client-side (i.e. javascript, php), converted to a json object (python), validated on the server-side (python), then stored into corresponding EAV database tables (python, mariadb).

When using the web-interface, it is important to ensure the csv, or xml file(s) are properly formatted. Dataset(s) poorly formatted will fail to create respective json dataset representation(s). Subsequently, dataset(s) will not succeed being stored in their correponding database tables.

The following provide examples of acceptable syntax:

- [csv sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/html/machine-learning/test/csv)
- [xml sample datasets](https://github.com/jeff1evesque/machine-learning/tree/master/html/machine-learning/test/xml)

###Programmatic Interface

When creating (sub)projects of this repository *programmatically*, it is important to leverage existing logic when possible:

- [Dataset Validation](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_validator.py)
- [Database methods](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_creator.py)

The same syntax requirement for csv, or xml file(s) to json conversion is required. This means logic contained within [`svm_json.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/svm_json.py) must be implemented if such files are used. However, if using a json object (dataset representation) directly is preferred, then no conversion logic is required. Simply ensure a list of dictionary elements:

```python
[{'dep_variable_label': 'xxx', 'indep_variable_label': 'xxx', 'indep_variable_value': yy.yy}]
```

is provided when inserting values into the EAV database tables. Exact syntax can be found in [`data_creator.py`](https://github.com/jeff1evesque/machine-learning/blob/master/python/data_creator.py). Be sure to validate the dataset(s) as needed before storing the dataset(s) in the database.

###Test Scripts
