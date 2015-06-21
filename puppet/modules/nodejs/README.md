# puppet-nodejs module

[![Build Status](https://travis-ci.org/puppet-community/puppet-nodejs.png)](http://travis-ci.org/puppet-community/puppet-nodejs)

#### Table of Contents

1. [Overview](#overview)
1. [Setup - The basics of getting started with nodejs](#setup)
    * [Beginning with nodejs - Installation](#beginning-with-nodejs)
1. [Usage](#usage)
1. [Npm packages](#npm-packages)
1. [Parameters](#parameters)
1. [Limitations - OS compatibility, etc.](#limitations)
    * [Module dependencies](#module-dependencies)
1. [Development](#development)

## Overview

The nodejs module installs the Node.js package, (global) npm package provider
and configures global npm configuration settings. A defined type nodejs::npm
is used for the local installation of npm packages.

By default this module installs packages from the [NodeSource](https://nodesource.com)
repository on Debian and RedHat platforms. The NodeSource Node.js package
includes the npm binary, which makes a separate npm package unnecessary.

On SUSE, ArchLinux, FreeBSD, OpenBSD and Gentoo, native packages are used. On
Darwin, the MacPorts package is used. On Windows the packages are installed
via Chocolatey.

## Setup

### What nodejs affects:

* the Node.js package
* the npm package (if it exists as a separate package)
* the global npmrc file ($PREFIX/etc/npmrc)
* globally installed npm packages
* local npm packages installed in user-specified directories

### Beginning with nodejs

To install Node.js and npm (using the NodeSource repository if possible):

```puppet
class { 'nodejs': }
```

If you wish to install a Node.js 0.12.x release from the NodeSource repository
rather than 0.10.x on Debian platforms:

```puppet
class { 'nodejs':
  repo_url_suffix => 'node_0.12',
}
```

## Usage

When a separate npm package exists (natively or via EPEL) the Node.js development
package also needs to be installed as it is a dependency for npm.

Install Node.js and npm using the native packages provided by the distribution:
(Only applicable for Ubuntu 12.04/14.04 and Fedora operating systems):

```puppet
class { '::nodejs':
  manage_package_repo       => false,
  nodejs_dev_package_ensure => 'present',
  npm_package_ensure        => 'present',
}
```

Install Node.js and npm using the packages from EPEL:

```puppet
class { '::nodejs':
  nodejs_dev_package_ensure => 'present',
  npm_package_ensure        => 'present',
  repo_class                => '::epel',
}
```

### npm packages

Two types of npm packages are supported:

* npm global packages are supported via the `npm` provider for the puppet
  package type.
* npm local packages are supported via the Puppet defined type nodejs::npm.

For more information regarding global vs local installation see the [nodejs blog](http://blog.nodejs.org/2011/03/23/npm-1-0-global-vs-local-installation/)

### npm global packages

The npm package provider is an extension of the Puppet package type which
supports versionable and upgradeable. The package provider only handles global
installation:

For example:

```puppet
package { 'express':
  ensure   => 'present',
  provider => 'npm',
}

package { 'mime':
  ensure   => '1.2.4',
  provider => 'npm',
}
```

### npm local packages

nodejs::npm is used for the local installation of npm packages. It attempts to
support all of the `npm install <package>` combinations shown in the
[npm install docs](https://docs.npmjs.com/cli/install)
except version ranges. The title simply must be a unique, arbitary value.

* If using packages directly off the npm registry, the package parameter is the
name of the package as published on the npm registry.
* If using scopes, the package parameter needs to be specified as
'@scope_name/package_name'.
* If using a local tarball path, remote tarball URL, local folder, git remote
URL or GitHubUser/GitRepo as the source of the package, this location needs
to be specified as the source parameter and the package parameter just needs
to be a unique, descriptive name for the package that is being installed.
* If using tags, the tag can be specified with the ensure parameter, and
the package parameter needs to be match the name of the package in the npm
registry.
* Package versions are specified with the ensure parameter, which defaults to
`present`.
* Install options and uninstall options are also supported, and need to be
specified as an array.
* The user parameter is provided should you wish to run npm install or npm rm
as a specific user.

nodejs::npm parameters:

* ensure: present (default), absent, latest, tag or version number.
* source: package source (defaults to a reserved value 'registry')
* target: where to install the package
* install_options: option flags invoked during installation such as --link (optional).
* uninstall_options: option flags invoked during removal (optional).
* npm_path: defaults to the value listed in `nodejs::params`
* user: defaults to undef

Examples:

Install the express package published on the npm registry to /opt/packages:

```puppet
nodejs::npm { 'express from the npm registry':
  ensure  => 'present',
  package => 'express',
  target  => '/opt/packages',
}
```
or the lazy way:

```puppet
nodejs::npm { 'express':
  target  => '/opt/packages',
}
```

Install the express package as user foo:

```puppet
nodejs::npm { 'express install as user foo':
  ensure  => 'present',
  package => 'express',
  target  => '/opt/packages',
  user    => 'foo',
}
```

Install a specific version of express to /opt/packages:

```puppet
nodejs::npm { 'express version 2.5.9 from the npm registry':
  ensure  => '2.5.9',
  package => 'express',
  target  => '/opt/packages',
}
```

Install the latest version of express to /opt/packages:

```puppet
nodejs::npm { 'express latest from the npm registry':
  ensure  => 'latest',
  package => 'express',
  target  => '/opt/packages',
}
```

Install express from GitHub to /opt/packages:

```puppet
nodejs::npm { 'express from GitHub':
  ensure  => 'present',
  package => 'express',
  source  => 'strongloop/express',
  target  => '/opt/packages',
}
```

Install express from a remote git repository to /opt/packages:

```puppet
nodejs::npm { 'express from a git repository':
  ensure  => 'present',
  package => 'express',
  source  => 'git+https://git@github.com/strongloop/expressjs.git',
  target  => '/opt/packages',
}
```

Install express from a remote tarball to /opt/packages:

```puppet
nodejs::npm { 'express from a remote tarball':
  ensure  => 'present',
  package => 'express',
  source  => 'https://server.domain/express.tgz',
  target  => '/opt/packages',
}
```

Install tagged packages:

```puppet
nodejs::npm { 'my beta tagged package':
  ensure  => 'beta',
  package => 'mypackage',
  target  => '/opt/packages',
}
```

Install a package from the registry associated with a specific scope:

```puppet
nodejs::npm { 'package_name from @scope_name':
  ensure  => 'present',
  package => '@scope_name/package_name',
  target  => '/opt/packages',
}
```

Install express from a local tarball to /opt/packages:

```puppet
nodejs::npm { 'express from a local tarball':
  ensure  => 'present',
  package => 'express',
  source  => '/local/repository/npm_packages/express.tgz',
  target  => '/opt/packages',
}
```

Install express with --save-dev --no-bin-links passed to `npm install`:

```puppet
nodejs::npm { 'express with options':
  ensure          => 'present',
  package         => 'express',
  install_options => ['--save-dev', '--no-bin-links'],
  target          => '/opt/packages',
}
```

Uninstall any versions of express in /opt/packages regardless of source:

```puppet
nodejs::npm { 'remove all express packages':
  ensure  => 'absent',
  package => 'express',
  target  => '/opt/packages',
}
```

### nodejs::npm::global_config_entry

nodejs::npm::global_config_entry can be used to set global npm configuration settings.

Examples:

```puppet
nodejs::npm::global_config_entry { 'proxy':
  ensure => 'present',
  value  => 'http://proxy.company.com:8080',
}
```

```puppet
nodejs::npm::global_config_entry { 'dev':
  ensure => 'present',
  value  => 'true',
}
```

Delete the key from all configuration files:

```puppet
nodejs::npm::global_config_entry { 'color':
  ensure => 'absent',
}
```

If a global_config_entry of `proxy` or `https-proxy` is specified, this will be
applied before the local installation of npm packages using `nodejs::npm`.

### Parameters

#### `cmd_exe_path`

Path to cmd.exe on Windows. Defaults to C:\Windows\system32\cmd.exe. You may
need to change this parameter for certain versions of Windows Server.

#### `legacy_debian_symlinks`

As per a Debian Technical Committee resolution (CTTE #614907), newer
native packages on Debian/Ubuntu changed the path of the Node.js
executable from /usr/bin/node to /usr/bin/nodejs. The nodejs-legacy package
creates symlinks in the event that one is running applications that require
the previous name. Setting this parameter to `true` recreates this behaviour.
The Node.js package in the NodeSource repository already creates this symlink
by default. This parameter defaults to `false`.

#### `manage_package_repo`

Whether to manage an external repository and use it as the source of the
Node.js and npm package. Defaults to `true`.

#### `nodejs_debug_package_ensure`

When set to `present` or a version number, determines whether to install the
Node.js package with debugging symbols, if available. Defaults to `absent`.

#### `nodejs_dev_package_ensure`

When set to `present` or a version number, determines whether to install the
development Node.js package, if available. Defaults to `absent`.

#### `nodejs_package_ensure`

When set to `present` or a version number, determines whether to install the
Node.js package. Defaults to `present`.

#### `npm_package_ensure`

When set to `present` or a version number, determines whether to install the
separate npm package. When using the NodeSource repository, the Node.js
package includes npm, so this value defaults to `absent`. This parameter will
need to be set to `present` if you wish to use the native packages or are
using the EPEL repository.

#### `npm_path`

Path to the npm binary.

#### `repo_class`

Name of the Puppet class used for the setup and management of the Node.js
repository. Defaults to `::nodejs::repo::nodesource` (NodeSource).
If using the Node.js and npm packages from the EPEL repository, set this to
`::epel` and make sure that the EPEL module is applied before the nodejs
module in your Puppet node definitions.

#### `repo_enable_src`

Whether any repositories which hold sources are enabled. Defaults to `false`.

#### `repo_ensure`

Whether to ensure that the repository exists, if it is being managed. Defaults
to `present` and may also be set to `absent`.

#### `repo_pin`

Whether to perform APT pinning to pin the Node.js repository with a specific
value. Defaults to `false`.

#### `repo_priority`

Whether to set a Yum priority for the Node.js repository. If using EPEL and
the NodeSource repository on the same system, you may wish to set this to a
value less than 99 (or the priority set for the EPEL repository) to ensure
that the NodeSource repository will always be preferred over the Node.js
packages in EPEL, should they both hold the same Node.js version. Defaults to
`absent`.

#### `repo_proxy`

Whether to use a proxy for this particular repository. For example,
http://proxy.domain . Defaults to `absent`.

#### `repo_proxy_password`

Password for the proxy used by the repository, if required.

#### `repo_proxy_username`

User for the proxy used by the repository, if required.

#### `repo_url_suffix`

This module defaults to installing the latest NodeSource 0.10.x release on
Debian platforms. If you wish to install a 0.12.x release you will need to
set this parameter to `node_0.12` instead.

#### `use_flags`

The USE flags to use for the Node.js package on Gentoo systems. Defaults to
['npm', 'snapshot'].

## Limitations

This module has received limited testing on:

* CentOS/RHEL 5/6/7
* Debian 7
* Fedora 20/21
* Ubuntu 10.04/12.04/14.04

The following platforms should also work, but have not been tested:

* Amazon Linux
* Archlinux
* Darwin
* Debian 8
* FreeBSD
* Gentoo
* OpenBSD
* OpenSuse/SLES
* Windows

This module is not supported on Debian Squeeze.

### Module dependencies

This module uses `treydock-gpg_key` for the import of RPM GPG keys. If using
an operating system of the RedHat-based family, you will need to ensure that
it is installed.

This modules uses `puppetlabs-apt` for the management of the NodeSource
repository. If using an operating system of the Debian-based family, you will
need to ensure that `puppetlabs-apt` version 2.x is installed.

If using CentoOS/RHEL 5, you will need to ensure that the `stahnma-epel`
module is installed.

If using CentoOS/RHEL 5/6/7 and you wish to install Node.js from EPEL rather
than from the NodeSource repository, you will need to ensure `stahnma-epel` is
installed and is applied before this module.

If using Gentoo, you will need to ensure `gentoo-portage` is installed.

If using Windows, you will need to ensure that `chocolatey-chocolatey` is
installed.

nodejs::npm has the ability to fetch npm packages from Git sources. If you
wish to use this functionality, Git needs to be installed and be in the
`PATH`.

## Development

Puppet Labs modules on the Puppet Forge are open projects, and community
contributions are essential for keeping them great. We can’t access the huge
number of platforms and myriad of hardware, software, and deployment
configurations that Puppet is intended to serve.

We want to keep it as easy as possible to contribute changes so that our
modules work in your environment. There are a few guidelines that we need
contributors to follow so that we can have a chance of keeping on top of
things.

Read the complete module [contribution guide](https://docs.puppetlabs.com/forge/contributing.html)
