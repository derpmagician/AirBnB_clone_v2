#!/usr/bin/python3
"""
Deletes out-of-date files. from servers
"""
from fabric.api import local, env, run, lcd

env.hosts = ['34.75.111.103', '18.206.176.219']


def do_clean(number=0):
    """
    Removes outdated files
    """
    n = int(number)
    if n < 0:
        return

    n = n + 1 if n > 0 else 2
    cmd = 'rm -rf $(ls -1t | tail -n+{})'.format(n)

    with lcd('versions'):
        local(cmd)

    with lcd('/data/web_static/releases'):
        run(cmd)
