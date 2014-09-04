Machine Learning
================

###Definition

###Overview

##Installation

###Linux Packages

The following packages need to be installed through terminal in Ubuntu:

```
# General Packages:

# Scikit Package(s):
sudo apt-get install python-numpy 
```

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

##Testing / Execution

###Test Scripts
