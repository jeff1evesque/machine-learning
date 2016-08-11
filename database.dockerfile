FROM container-default

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## provision with puppet
RUN cat $ENVIRONMENT_DIR/manifests/setup_database.pp
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/manifests/setup_database.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/test

## executed everytime container starts
CMD ["mysqld"]