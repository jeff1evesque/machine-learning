FROM ml-base

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## copy files into container
COPY . /var/machine-learning

## install pytest-cov
RUN pip install pytest-cov==2.4.0

## provision with puppet
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/sklearn/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/compiler/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/webserver/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT

## executed everytime container starts
WORKDIR /var/machine-learning
ENTRYPOINT ["python", "app.py"]