#!/usr/bin/python3

from fabric.api import *
import os.path

env.hosts = ['34.74.248.124', '35.237.140.145']


def do_deploy(archive_path):
    ''' deploy '''
    if os.path.isfile(archive_path):
        name = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(name))
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{0} -C /data/web_static/releases/{0}/'.format(name))
        run('rm /tmp/{}'.format(name))
        run('mv /data/web_static/releases/{0}/web_static/*\
        /data/web_static/releases/{0}/'.format(name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(name))
        print('New version deployed!')
        return True
    else:
        return False
