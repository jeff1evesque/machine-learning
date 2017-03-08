FROM container-default

## local variables
ENV ROOT_PROJECT /var/machine-learning
ENV ENVIRONMENT docker
ENV ENVIRONMENT_DIR $ROOT_PROJECT/puppet/environment/$ENVIRONMENT

## provision with puppet
RUN pip install -y pyyaml
RUN /opt/puppetlabs/bin/puppet apply $ENVIRONMENT_DIR/modules/webserver/manifests/init.pp --modulepath=$ENVIRONMENT_DIR/modules_contrib:$ENVIRONMENT_DIR/modules --confdir=$ROOT_PROJECT/hiera/test

## executed everytime container starts
WORKDIR /var/machine-learning
ENTRYPOINT ["python", "app.py"]