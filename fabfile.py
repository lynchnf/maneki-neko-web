from fabric.api import *
import os

def pack():
    local("cd /tmp/")
    local("rm -rf maneki-neko-web")
    local("rm -rf maneki-neko-web.tgz")
    local("git clone git@github.com:lynchnf/maneki-neko-web.git")
    local("tar cfz maneki-neko-web.tgz maneki-neko-web")
    

def deploy():
    pack()
    put("/tmp/maneki-neko-web.tgz", "maneki-neko-web.tgz")
    run("tar xfz maneki-neko-web.tgz -m")
    sudo("rm -rf /var/www/maneki-neko-web")
    sudo("mv maneki-neko-web /var/www")
    #sudo("rm %s%s/pack575/settings.py" % (base_dir, project))
    #sudo("mv %s%s/pack575/settings_prod.py %s%s/pack575/settings.py" % (base_dir, project, base_dir, project))
    sudo("chown -R www-data:www-data /var/www/maneki-neko-web")
    sudo("chmod -R g+w /var/www/maneki-neko-web")
    sudo("source /root/mnweb/bin/activate")
    #sudo("chown -R www-data:www-data %s%s" % (base_dir, static))
    #sudo("chmod -R g+w %s%s" % (base_dir, static))
    #sudo("cd /var/www/%s/; python manage.py migrate portal" % (project))
    sudo('/etc/init.d/apache2 reload')