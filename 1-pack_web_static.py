#!/usr/bin/python3
""" Compress webstatic"""

from fabric.api import local
from datetime import datetime as dt
import os


now = dt.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}.tgz'\
                .format(now.strftime("%Y%m%d%H%M%S"))

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    command = local("tar -cvzf {} web_static".format(file_name))
    if command.succeeded:
        return file_name
    return None
