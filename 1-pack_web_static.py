#!/usr/bin/python3

from fabric.api import local
import datetime


def do_pack():
    '''Function for generate pack all files'''
    actual = datetime.datetime.now()
    local('mkdir -p versions/')
    pack = 'versions/web_static_{}{}{}{}{}.tgz'.format(
                    actual.year, actual.month,
                    actual.day, actual.minute, actual.second)
    local('sudo tar -cvzf {} web_static'.format(pack))
    if pack:
        return pack
    return None
