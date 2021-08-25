#!/usr/bin/python3
""" Compress webstatic"""

from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """
    Generates a .tgz archive of the web_static folder of this repo
    """    

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_" + date + ".tgz"

    try:
        if path.exists("versions") is False:
            local("mkdir versions")
        local("tar -zcvf {} web_static".format(name))
        return name
    except:
        return None
