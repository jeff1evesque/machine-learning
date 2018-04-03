FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV ROOT_PROJECT /var/machine-learning
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ARG NGINX_NAME

## copy files into container
COPY hiera $ROOT_PROJECT/hiera
COPY puppet/environment/$ENVIRONMENT/modules/nginx $ROOT_PUPPET/code/modules/nginx

## provision with puppet
RUN $PUPPET apply -e "class { nginx: \
    type           => 'web', \
    vhost          => 'machine-learning.com', \
    host_port      => '8080', \
    listen_port    => '5000', \
    webserver_port => '5001', \
    proxy => 'http://localhost' \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## start nginx
CMD ["/bin/sh", "-c", "nginx"]
