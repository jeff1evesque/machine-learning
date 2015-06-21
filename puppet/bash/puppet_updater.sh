#!/bin/bash

if [ ! -e /tmp/puppet-updated ]; then
  wget -O /tmp/puppetlabs-release-trusty64.deb http://apt.puppetlabs.com/puppetlabs-release-trusty.deb
  dpkg -i /tmp/puppetlabs-release-trusty64.deb
  apt-get update
  apt-get --assume-yes install puppet
  touch /tmp/puppet-updated
fi