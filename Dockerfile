FROM ubuntu:14.04

## install puppet
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
RUN dpkg -i puppetlabs-release-trusty.deb

## update package manager
RUN apt-get update

## install r10k
RUN apt-get install rubygems-integration
RUN gem install r10k
