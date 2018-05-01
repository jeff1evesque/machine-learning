FROM jeff1evesque/ml-base:0.7

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
ARG MEMBERS

## copy files into container
COPY hiera.yaml $ROOT_PUPPET/puppet/hiera.yaml
COPY hiera/reverse-proxy/nginx-$TYPE.yaml $ROOT_PUPPET/puppet/hiera/reverse-proxy/nginx.yaml
COPY puppet/environment/$ENVIRONMENT/modules/reverse_proxy $ROOT_PUPPET/code/modules/reverse_proxy

##
## provision with puppet: either build a web, or api nginx image.
##
##     docker build --build-arg TYPE=api --build-arg RUN=false --build-arg VHOST=machine-learning-api.com --build-arg HOST_PORT=9090 --build-arg LISTEN_PORT=6000 -f nginx.dockerfile -t jeff1evesque/ml-nginx-api:0.7 .
##     docker build --build-arg TYPE=web --build-arg RUN=false --build-arg VHOST=machine-learning-web.com --build-arg HOST_PORT=9090 --build-arg LISTEN_PORT=6000 -f nginx.dockerfile -t jeff1evesque/ml-nginx-web:0.7 .
##
##     docker build --build-arg TYPE=api --build-arg RUN=false -f nginx.dockerfile -t jeff1evesque/ml-nginx-api:0.7 .
##     docker build --build-arg TYPE=web --build-arg RUN=false -f nginx.dockerfile -t jeff1evesque/ml-nginx-web:0.7 .
##
##     docker run --hostname nginx-api --name nginx-api -d jeff1evesque/ml-nginx-api:0.7
##     docker run --hostname nginx-web --name nginx-web -d jeff1evesque/ml-nginx-web:0.7
##
RUN $PUPPET apply -e "class { reverse_proxy: \
    run => 'false', \
} " --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet

## start nginx
CMD ["nginx", "-g", "daemon off;"]
