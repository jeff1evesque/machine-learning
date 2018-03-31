FROM ml-base

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV PUPPET /opt/puppetlabs/bin/puppet
ENV ROOT_PUPPET /etc/puppetlabs
ENV MODULES $ROOT_PUPPET/code/modules
ENV CONTRIB_MODULES $ROOT_PUPPET/code/modules_contrib
ARG NGINX_NAME

##
## environment variables
##
##     build cases: non-persistent hostname
##
##     docker build --build-arg NGINX_NAME=nginx-api -f nginx.dockerfile -t ml-nginx-api .
##     docker build --build-arg NGINX_NAME=nginx-web -f nginx.dockerfile -t ml-nginx-web .
##
##     run cases: persistent hostname
##
##     docker run --hostname nginx-api --name nginx-api -d ml-nginx-api
##     docker run --hostname nginx-web --name nginx-web -d ml-nginx-web
##
## @HOSTNAME, build time argument, used to temporarily set the hostname, to
##     allow nginx to be installed, with respective host parameters.
##
## Note: inline edits to '/etc/hosts', via 'docker build' is not persistent.
##
RUN echo $(grep $(hostname) /etc/hosts | cut -f1) ${NGINX_NAME} >> /etc/hosts && \
    echo ${NGINX_NAME} > /etc/hostname && \
    $PUPPET apply $MODULES/modules/nginx/manifests/init.pp --modulepath=$CONTRIB_MODULES:$MODULES --confdir=$ROOT_PUPPET/puppet


## start nginx
CMD ["/bin/sh", "-c", "nginx"]
