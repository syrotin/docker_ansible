#!/usr/bin/python

import os
import time

def instansible():
   os.system('apt update && apt install dirmngr -y')
   os.system('echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list')
   os.system('apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367')
   os.system('apt update && apt install ansible -y')

def instdocker():
    os.system('apt-get remove docker docker-engine docker.io')
    os.system('apt-get update')
    os.system('apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y')
    os.system('curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -')
    os.system('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"')
    os.system('apt-get update')
    os.system('apt-get install docker-ce git docker-compose -y')


instansible()
instdocker()
