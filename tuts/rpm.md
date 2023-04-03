# RPM 
## commands

Yellow Dog Updater, Modified (YUM)
DNF or Dandified YUM is the updated default since Red Hat Enterprise Linux 8, CentOS 8, Fedora 22, and any distros based on these.
YUM is the primary package management tool for redhat.
YUM performs dependency resolution when installing, updating, and removing software packages. 
YUM can manage packages from installed repositories in the system or from .rpm packages. 

```bash
# you can see all the options using
yum -option

# To see the past work done related to packages
yum history

# We can simply undo or redo any action using
yum history [undo/redo] transaction_num

# ex : it will undo transaction 6
yum history undo 6

# Install and remove a package
yum install ksh -y 
yum remove ksh

```

DNF 
DNF stands for "Dandified Yum" and it is a software package manager 
used to install, update, and remove packages in the operating system. 
It is a replacement for the older Yum package manager used in earlier versions of RHEL.

```bash

# lists all packages that are available in the enabled repositories.
dnf list available

# update or upgrade packages
dnf update/upgrade

# update specific package
dnf update package_name

# install
dnf install package.name 

# get info of a package
dnf info package.name

# list installed packages
dnf list installed

# remove or uninstall
dnf remove package.name

# search for a package in the repositories which are enabled
dnf search package

# check for updates
dnf check-update

# enable repository
dnf config-manager --enable repository_name

# disable repo
dnf config-manager --disable repository_name

# clean up package cache
dnf clean packages

# install package group
dnf group install group_name
# ex
dnf group install "Development Tools"

# lists all available package groups.
dnf group list

# We can simply undo or redo any action using
yum history [undo/redo] transaction_num

```
Subscription Manager
Subscription-manager is a command-line tool used in (RHEL) to manage software subscriptions, entitlements, and registrations.

```bash

# Register a system
subscription-manager register

# List available subscription
subscription-manager list --available

# Attaching a subscription
subscription-manager attach --pool=pool_id

# List subscribed product
subscription-manager list --consumed

# Unsubscribe from a product
subscription-manager unsubscribe --serial=serial_number

# Check subscription status
subscription-manager status

# Refreshing subscription information
subscription-manager refresh

# Viewing system identity
subscription-manager identity

# enable a repo
subscription-manager repos --enable=repository_id

# disable a repo
subscription-manager repos --disable=repository_id


```


RPM (RPM Package Manager)
RPM is a popular package management tool redhat based distros
Using RPM, you can install, uninstall, and query individual software packages.
Issue: It cannot manage dependency resolution like YUM.
RPM maintains a database of installed packages, which enables powerful and fast queries.
Some commonly used modes

RPM
-i install
-U upgrade
-e erase
-V verify
-q query

Note 
To install or upgrade an .rpm package using RPM, issue this command:
You need to first download .rpm package

```bash
# Install
rpm -i package-file

# Update
rpm -U package-file

# (v-verbose, h for hash to show progress)
rpm -ivh package-file 

# Erase
rpm -evh package-file

# Query all the installed packages
rpm -qa

# More info about the package
rpm -qi package_name

# Info about config files for a package
rpm -qc package_name

```

<br>
