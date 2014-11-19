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
sudo apt-get install lamp-server^ phpmyadmin
sudo apt-get install inotify-tools
sudo pip install jsonschema
sudo pip install python-magic

# Latest PPA for nodejs:
curl -sL https://deb.nodesource.com/setup | sudo bash -

# nodejs / npm:
sudo apt-get install nodejs
sudo apt-get install npm

# Compiler / Minifier:
sudo gem install sass
sudo npm install uglify-js -g
sudo npm install --global imagemin

# Scikit-Learn Dependency:
sudo apt-get install python-numpy
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system.

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
cd /var/www/html/machine-learning/
git remote add upstream https://github.com/[YOUR-USERNAME]/machine-learning.git
```

####GIT Submodule

We need to initialize our git *submodules*:

```
sudo git submodule init
sudo git submodule update
```

**Note:** We have to use the *sudo* prefix, since we haven't taken care of file permissions yet.

The above two commands will update submodules.  If they are already initialized, then the latter command will suffice. Then, we need to pull the code-base into the initialized submodule directory:

```
cd /var/www/
git checkout -b NEW_BRANCH master
cd [YOUR_SUBMODULE]/
git checkout master
git pull
cd ../
git status
```

Now, commit and merge the submodule changes.

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
cd /var/www/html/bash/
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

[jQuery Validation](http://jqueryvalidation.org/) is a plugin that allows [client-side](http://en.wikipedia.org/wiki/Client-side) validation on [HTML form](http://www.w3.org/TR/html5/forms.html) elements. When a specific field fails validation, a label element is created as the next successive [DOM](http://en.wikipedia.org/wiki/Document_Object_Model) element, indicating an *error message*.

The following provides additional documentation on the jQuery plugin:

- http://jqueryvalidation.org/documentation/
- http://jqueryvalidation.org/category/validator/
- http://jqueryvalidation.org/jQuery.validator.addMethod/
- http://stackoverflow.com/questions/10843399#answer-10843593

This project implements client-side validation within [`form_validator.js`](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js). Specific *how-to* can be found within the comments of the javascript [code](https://github.com/jeff1evesque/machine-learning/blob/master/src/js/form_validator.js).

**Note:** this project *may* implement concepts of *machine learning*, where data is not supplied via an HTML form. If data is not supplied by the user (HTML form), then backend-validation (refer to [*JSON Schema*](https://github.com/jeff1evesque/machine-learning/blob/c5f6179870ed475c2cdac0aaae8f839b6f571840/README.md#json-schema)) becomes even more crucial.

###JSON Schema

##Testing / Execution

###Test Scripts
