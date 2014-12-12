from fabric.api import *
import os
base_dir = '/var/www/'
project = 'maneki-neko-con'
static = '%s/static' % project

def pack():
    local("rm -f /tmp/%s.tgz" % (project))
    local("rm -rf /tmp/%s" % (project))
    local("git clone . /tmp/%s" % (project))
    local("cd /tmp/; tar cfz /tmp/%s.tgz %s" % (project, project))
    

def deploy():
    pack()
    put("/tmp/%s.tgz" % (project), "%s.tgz" % (project))
    run("tar xfz %s.tgz -m" % (project))
    sudo("rm -rf %s%s" % (base_dir,project))
    sudo("mv %s %s" % (project, base_dir))
    sudo("cp /tmp/project.db %s%s/project.db" % (base_dir, project))
    sudo("rm %s%s/pack575/settings.py" % (base_dir, project))
    sudo("mv %s%s/pack575/settings_prod.py %s%s/pack575/settings.py" % (base_dir, project, base_dir, project))
    sudo("chown -R www-data:www-data %s%s" % (base_dir, project))
    sudo("chmod -R g+w %s%s" % (base_dir, project))
    sudo("source /usr/local/pythonenv/scouts/bin/activate; cd /var/www/%s/; echo 'yes' | python manage.py collectstatic" % (project))
    sudo("chown -R www-data:www-data %s%s" % (base_dir, static))
    sudo("chmod -R g+w %s%s" % (base_dir, static))
    #sudo("cd /var/www/%s/; python manage.py migrate portal" % (project))
    sudo('/etc/init.d/apache2 reload')
    
def deploy_dev():
    deploy()
    sudo("cp %s%s/local_settings_pscilvorcl02.py %s%s/local_settings.py" % (base_dir, project, base_dir, project))
