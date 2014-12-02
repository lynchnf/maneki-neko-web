maneki-neko-web
===============

Content Management System for science fiction/fantasy convention websites. It will include modules for on-line registration, etc.

Project install instructions tested on Ubuntu 14.04.1 LTS (64 bit).

1. Update apt-get.
  - `sudo apt-get update`

2. Install MySQL.
  - `sudo apt-get install mysql-server`

3. Install other crap we'll need.
  - `sudo apt-get install python-dev`
  - `sudo apt-get install libmysqlclient-dev`
  - `sudo apt-get install libjpeg-dev`
  - `sudo apt-get install default-jre`

4. Create database and user.
  - `mysql --user=root --password=********`
  - `create user mnwebuser identified by 'swordfish';`
  - `create database mnwebdb;`
  - `grant all on mnwebdb.* to mnwebuser;`
  - `exit`

5. Install dbvisualizer. (optional)
  - Browse to [dbvis.com](http://www.dbvis.com/).
  - Download Linux setup installer.
  - `chmod 777 dbvis_linux_9_1_10.sh`
  - `sudo ./dbvis_linux_9_1_10.sh`
  - Install in directory /opt/DbVisualizer.

6. Install Git.
  - `sudo apt-get install git`
  - `git config --global user.name "Your Name Here"`
  - `git config --global user.email your_email@example.com`
  - `git config --global push.default simple`
  - Make sure you have ssh keys.

7. Install Eclipse. (optional)
  - `sudo apt-get install eclipse`
  - Open Eclipse.
  - Help > Install New Software....
  - Add site > http://pydev.org/updates.
  - Select and install PyDev.
  - Trust the certificates.
  - Exit Eclipse.

8. Install pip.
  - `sudo apt-get install python-pip`
  - `sudo pip install -U pip`

9. Setup virtual environment.
  - `sudo pip install virtualenv`
  - `virtualenv mnweb`
  - `source mnweb/bin/activate`

10. Get project source.
  - `cd ~/workspace`
  - `git clone git@github.com:lynchnf/maneki-neko-web.git`
  - `cd ~/workspace/maneki-neko-web`
  - `git checkout development`
  

11. Build and run project.
  - `cd ~/workspace/maneki-neko-web`
  - `pip install -r requirements.txt`
  - `python manage.py syncdb --all`
  - `python manage.py migrate --fake`
  - `python manage.py runserver`

12. Restart Eclipse.
  - Window > Preferences > PyDev > Interpreter > Python
  - New...
  - Interpreter Name: mnweb
  - Interpreter Executable: mnweb/bin/python
  - Ok > Ok > Ok
  - File > New > Project... > PyDev Project
  - Project name: maneki-neko-web
  - Interpreter: mnweb
  - Finish