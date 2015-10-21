FROM ubuntu:14.04

## install git, and wget
RUN apt-get update -y
RUN apt-get install git -y
RUN apt-get install wget -y

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
RUN dpkg -i puppetlabs-release-trusty.deb
RUN apt-get update -y

## install r10k
RUN apt-get install rubygems-integration -y
RUN gem install r10k

## clone repository: allow puppet manifests to run (below)
RUN git clone https://jeff1evesque@github.com/jeff1evesque/machine-learning.git /var/machine-learning

## install puppet modules using puppetfile with r10k
RUN mkdir /var/machine-learning/puppet/modules/
RUN PUPPETFILE=/var/machine-learning/puppet/scripts/Puppetfile PUPPETFILE_DIR=/var/machine-learning/puppet/modules/ r10k puppetfile install

## debug print
RUN ls -l /var/machine-learning
RUN ls -l /var/machine-learning/puppet/modules

## provision with puppet
RUN find /var/machine-learning/puppet/manifests -type f -name '*.pp' -exec puppet apply {} \;
