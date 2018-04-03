FROM ml-base

## local variables
ENV ENVIRONMENT docker
ENV ROOT_PROJECT /var/machine-learning
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ARG TYPE
ARG VHOST
ARG HOST_PORT
ARG LISTEN_PORT
ARG WEBSERVER_PORT

## copy files into container
COPY hiera $ROOT_PROJECT/hiera
COPY puppet/environment/$ENVIRONMENT/modules/nginx $ROOT_PUPPET/code/modules/nginx

## provision with puppet: either build a web, or api nginx image.
##
##     docker build --build-arg TYPE=web --build-arg VHOST=machine-learning.com --build-arg HOST_PORT=8080 --build-arg LISTEN_PORT=5000 --build-arg WEBSERVER_PORT=5001 -f nginx.dockerfile -t ml-nginx-web .
##     docker build --build-arg TYPE=api --build-arg VHOST=machine-learning-api.com --build-arg HOST_PORT=9090 --build-arg LISTEN_PORT=6000 --build-arg WEBSERVER_PORT=6001 -f nginx.dockerfile -t ml-nginx-api .
##
##     docker run --hostname nginx-api --name nginx-api -d ml-nginx-api
##     docker run --hostname nginx-web --name nginx-web -d ml-nginx-web
##
RUN $PUPPET apply -e "class { nginx: \
    type           => 'web', \
    vhost          => 'machine-learning.com', \
    host_port      => '8080', \
    listen_port    => '5000', \
    webserver_port => '5001', \
    proxy          => 'http://localhost' \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## start nginx
CMD ["/bin/sh", "-c", "nginx"]
