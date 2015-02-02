Production Environment Setup
============================

Follow the instructions below to setup a production environment and deploy the project from your development environment.

You will need a domain registrar (I used GoDaddy) and a hosting provider (I used DigitalOcean).

1. Buy a domain.
  - Find domain registar you like and buy a domain.
  
2. Buy hosting space.
  - Find a hosting provider you like and buy hosting space.
  - Create a virtual server. (Your provider may call it an instance or droplet or something else).
  - Choose an operation system for your virtual server. (I used Ubuntu 14.04.1 LTS (64 bit).)

3. Log in to your new virtual server.
  - Your hosting provider will probably email you the ip address and root password for your new virtual server.
  - Log in to your new virtual server. If you use a Windows machine, you will need a tool like PuTTY.
  - Change your root password. My server automatically prompted me to change it.
  
4. Create a webmaster user.
  - `adduser webmaster`
  - `visudo`
  - Add "webmaster" under user privilege specification section.
  - Save and exit.
  - `exit`

5. Apply updates.
  - Log in to your virtual server as webmaster.
  - `sudo apt-get clean`
  - `sudo apt-get update`
  - `sudo apt-get upgrade`
  - `sudo apt-get dist-upgrade`
  - `sudo reboot`
  
6. Install Apache.
  - Log in to your virtual server as webmaster.
  - `sudo apt-get install apache2`
  - `sudo adduser webmaster adm`
  - browse to your virtual server's ip address to verify apache is running

7. Bind your virtual server's ip address to your domain.
  - Log in to your domain registar
  - Change the nameservers for your domain to the nameservers provided by your hosting provider.
  - Log in to your hosting provider.
  - Add a your domain to your virtual server. This should create a zone file for your domain name.
  - Your zone file should have 2 or 3 NS records with your hosting providers nameservers.
  - Your zone file should have a A record with a name of @ and your virtual server's ip address.
  - Your zone file should have another A record with a name of www and your virtual server's ip address.
  - Wait 2 hours.
  - Browse to your domain name to verify it works.
  
8. Install MySQL.
  - Log in to your virtual server as webmaster.
  - `sudo apt-get install mysql-server`
  
9. Create database and user.
  - `mysql --user=root --password=********`
  - `create user mnwebuser identified by 'xxxxxxxx';`
  - `create database mnwebdb;`
  - `grant all on mnwebdb.* to mnwebuser;`
  - `exit`
  
10. Install other stuff we'll need.
  - `sudo apt-get install python-dev`
  - `sudo apt-get install libmysqlclient-dev`
  - `sudo apt-get install libjpeg-dev`
  - `sudo apt-get install libapache2-mod-wsgi`
  
11. Install pip.
  - `sudo apt-get install python-pip`
  - `sudo pip install -U pip`
  
12. Create a virtual environment.
  - `sudo pip install virtualenv`
  - `cd ~`
  - `virtualenv mnweb`

13. Deploy the project to get the pip requirements.
  - Login to your development machine.
  - `source mnweb/bin/activate`
  - `cd workspace/maneki-neko-web`
  - `fab deploy'
  - When it asks for a single host string for connection, reply with webmaster@<your domain>.
  - You will get an error saying 'Fatal error on "mv /var/www/maneki-neko-web/media /tmp/maneki-neko-web"'.
  
14. Update virtual environment.
  - Log in to your virtual server as webmaster.
  - `source mnweb/bin/activate`
  - `sudo mv /tmp/maneki-neko-web /var/www`
  - `cd /var/www/maneki-neko-web`
  - `pip install -r requirements.txt`
  
15. Create a production settings file.
  - `cp /var/www/maneki-neko-web/website/env_settings.py ~/maneki-neko-web-settings.py`
  
16. Generate a secret key for your production settings.  
  - `cd ~`
  - `django-admin.py startproject junk`
  - `cat ~/junk/junk/settings.py`
  - Copy the secret key.
  - `nano ~/maneki-neko-settings.py`
  - Paste the secret key.
  
17. Change other production settings.
  - DEBUG and TEMPLATE_DEBUG should be False.
  - ALLOWED_HOSTS should be your host names, e.g. ["domain.com", "www.domain.com"].
  - Update password for database.
  - Change location of log file to /var/log/maneki-neko-web/website.log.
  - Change log levels to WARN.
  - Save and exit.
  - `rm -rf junk`
  
18. Setup logging.  
  - `cd /var/log/`
  - `sudo mkdir maneki-neko-web`
  - `sudo chmmod 777 maneki-neko-web`
  - `cd maneki-neko-web`
  - `sudo touch website.log`
  - `sudo chmod 666 website.log`
  - `cd /etc/logrotate.d`
  - `sudo nano maneki-neko-web`
  - Enter the following, then save and exit:
```
    /var/log/maneki-neko-web/*.log {
        daily
        rotate 30
    }
```

cd /etc/apache2/sites-available/
sudo cp 000-default.conf maneki-neko-web.conf
sudo nano maneki-neko-web.conf
edit config file
save and exit
sudo a2ensite maneki-neko-web.conf

cd /var/www/maneki-neko-web
mkdir media

login to your development machine
source mnweb/bin/activate
cd workspace/maneki-neko-web
fab deploy

Use putty to login as webmaster.
source mnweb/bin/activate
cd /var/www/maneki-neko-web
python manage.py syncdb --all
    7) Create a super user named webmaster
    8) Need to create another god damn new password.
python manage.py migrate --fake

browse to website admin
edit site record
add home page
