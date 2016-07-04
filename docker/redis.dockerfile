## custom container built locally
FROM container-default

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply /var/machine-learning/puppet/environment/development/manifests/configure_redis.pp --modulepath=/var/machine-learning/puppet/environment/development/modules_contrib:/var/machine-learning/puppet/environment/development/modules --confdir=/var/machine-learning/test
