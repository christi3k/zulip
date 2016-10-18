# Development environment installation

Zulip support a wide range of ways to install the Zulip development
environment. **We recommend using the [Vagrant development
environment][rtd-vagrant-setup], since it is easiest to
setup and uninstall.**

If you have a very slow network connection, however, you may want to avoid
using Vagrant (which involves downloading an Ubuntu image) and
either [install directly][rtd-install-direct] if you are
using Ubuntu 14.04 or 16.04 or else use [the manual install
process][rtd-install-direct] instead. Note that those options only
support Linux-based operating systems and won't work with OS X or Windows.

An alternative option with poor network connectivity is to rent a
cloud server (with at least 2GB of RAM), install the development
environment there (we'd recommend the
[install directly][rtd-install-direct] approach),
and connect to the development environment over SSH.

While Zulip itself is built and deployed on Ubuntu, the Zulip developer
environment is cross-platform and can be installed on most all current
operating systems. Use the operating system that you are most familiar with.

### For OS X

The [Vagrant environment setup][rtd-vagrant-setup] is recommended for all
contributors. If you are already using Docker and like it, you can try [using
Docker (experimental)](install-docker-dev.html), but know this isn't officially
supported by Zulip.

### For Ubuntu

The [Vagrant environment setup][rtd-vagrant-setup] is recommended for all
contributors. If you prefer to work without Vagrant, you can [install directly
on Ubuntu][rtd-install-direct]. You need Ubuntu 14.04 Trusty or Ubuntu 16.04
Xenial for direct installation to work. If you are already using Docker and
like it, you can try [using Docker (experimental)](install-docker-dev.html),
but know this isn't officially supported by Zulip.

### For Other Linux/Unix-based Platforms

You'll have to [install the developer environment
manually][rtd-install-generic]. If you are already using Docker and like it,
you can try [using Docker (experimental)](install-docker-dev.html), but know
this isn't officially supported by Zulip.

### For Windows

The [Vagrant environment setup][rtd-vagrant-setup] is recommended for all
contributors and is the only supported way to install on Windows.

## Using the Development Environment & Testing

Once you've installed the Zulip development environment, you'll want
to read these documents to learn how to use it:

* [Using the Development Environment](using-dev-environment.html)
* [Testing](testing.html)

[rtd-vagrant-setup]: dev-env-first-time-contributors.html
[rtd-install-direct]: install-ubuntu-without-vagrant-dev.html
[rtd-install-generic]: install-generic-unix-dev.html
