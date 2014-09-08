Machine Learning
================

###Definition

Machine learning is a [subfield](http://en.wikipedia.org/wiki/Academic_disciplines) of [computer science](http://en.wikipedia.org/wiki/Computer_science) (CS) and [artificial intelligence](http://en.wikipedia.org/wiki/Artificial_intelligence) (AI) that deals with the construction and study of systems that can [learn](http://en.wikipedia.org/wiki/Learning) from data, rather than follow only explicitly programmed instructions.

Applications for machine learning include:

<ul>
  <li>[Object recognition](http://en.wikipedia.org/wiki/Object_recognition)</li>
  <li>[Natural language processing](http://en.wikipedia.org/wiki/Natural_language_processing)</li>
  <li>[Search engines](http://en.wikipedia.org/wiki/Search_engines)</li>
  <li>[Bioinformatics](http://en.wikipedia.org/wiki/Bioinformatics)</li>
  <li>[Stock market](http://en.wikipedia.org/wiki/Stock_market) analysis</li>
  <li>[Speech](http://en.wikipedia.org/wiki/Speech_recognition) and [handwriting recognition](http://en.wikipedia.org/wiki/Speech_recognition)</li>
  <li>[Sentiment analysis](http://en.wikipedia.org/wiki/Sentiment_analysis)</li>
  <li>[Recommender systems](http://en.wikipedia.org/wiki/Recommender_system)</li>
  <li>[Sequence mining](http://en.wikipedia.org/wiki/Sequence_mining), commonly referred as *data mining*</li>
  <li>[Computational advertising](http://en.wikipedia.org/wiki/Computational_advertising), and [Computational finance](http://en.wikipedia.org/wiki/Computational_finance)</li>
</ul>

- http://en.wikipedia.org/wiki/Machine_learning

In [machine learning](http://en.wikipedia.org/wiki/Machine_learning), support vector machines (SVMs) are [supervised learning](http://en.wikipedia.org/wiki/Supervised_learning) models with associated learning [algorithms](http://en.wikipedia.org/wiki/Algorithm) that analyze data and recognize patterns, used for [classification](http://en.wikipedia.org/wiki/Statistical_classification) and [regression analysis](http://en.wikipedia.org/wiki/Regression_analysis). 

- http://en.wikipedia.org/wiki/Support_vector_machine

###Overview

##Installation

###Linux Packages

The following packages need to be installed through terminal in Ubuntu:

```
# General Packages:

# Scikit Package(s):
sudo apt-get install python-numpy 
```

**Note:** This project assumes [Ubuntu Server 14.04](http://www.ubuntu.com/download/server) as the operating system.

##Configurations

###GIT

Fork this project in your GitHub account, then clone your repository:

```
cd /var/www/html/
sudo git clone https://[YOUR-USERNAME]@github.com/[YOUR-USERNAME]/machine-learning.git machine-learning
```

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
cd /var/www/html/machine-learning/
git checkout -b NEW_BRANCH master
cd [YOUR_SUBMODULE]/
git checkout master
git pull
cd ../
git status
```

Now, commit and merge the submodule changes.

###File Permission

Change the file permission for the entire project by issuing the command:

```
cd /var/www/html/
sudo chown -R jeffrey:sudo machine-learning
```

**Note:** change 'jeffrey' to the user account YOU use.

##Testing / Execution

###Test Scripts
