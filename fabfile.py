from fabric.api import env, run, cd, local, sudo

env.user = 'ubuntu'
env.hosts = ['easyform.dxetech.com']
remote_path = '/home/ubuntu/python/easy-form'

def deploy():
    local('git push origin master')
    with cd(remote_path):
        run('git pull')
        run('venv/bin/pip install -r requirements.txt')
    sudo('service restart easyform')
