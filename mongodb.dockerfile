FROM container-default

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## basic configuration
USER mongodb
WORKDIR /var/lib/mongodb
VOLUME ["/data/db"]

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/mongodb/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test

## executed everytime container starts
ENTRYPOINT ["/usr/bin/mongod", "--config", "/etc/mongod.conf"]
CMD ["--quiet"]