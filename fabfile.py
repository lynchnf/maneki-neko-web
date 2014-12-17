from fabric.api import *
import os

def pack():
    local("rm -rf /tmp/maneki-neko-web")
    local("git clone git@github.com:lynchnf/maneki-neko-web.git /tmp/maneki-neko-web")
    local("rm -rf /tmp/maneki-neko-web.tgz")
    local("cd /tmp; tar cfz maneki-neko-web.tgz maneki-neko-web")

def deploy():
    pack()
    put("/tmp/maneki-neko-web.tgz", "/tmp/maneki-neko-web.tgz")
    run("cd /tmp; tar xfz maneki-neko-web.tgz -m")
    sudo("rm -rf /var/www/maneki-neko-web")
    sudo("mv /tmp/maneki-neko-web /var/www/")
    sudo("cp /var/www/maneki-neko-web/website/settings.py ~/maneki-neko-dev-settings.py")
    sudo("cp ~/maneki-neko-prod-settings.py /var/www/maneki-neko-web/website/settings.py")
    sudo("chown -R www-data:www-data /var/www/maneki-neko-web")
    sudo("chmod -R g+w /var/www/maneki-neko-web")
    sudo('/etc/init.d/apache2 reload')
