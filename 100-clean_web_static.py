#!/usr/bin/python3
"""
Deletes out-of-date files. from servers
"""
from fabric.api import local, env, run

env.hosts = ['34.75.111.103', '18.206.176.219	']


def do_clean(number=0):
    """
    Select how the number of files to keep
    """
    number = 2 if number < 1 else number + 1
    local("ls -d -1t versions/* | tail -n +{} | \
    xargs -d '\n' rm -f".format(number))

    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
    xargs -d '\n' rm -rf".format(number))
