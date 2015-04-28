Regular Operations
==================

On a regular basis (at least weekly, maybe daily), log in to your server as webmaster and do the following:

1. Install updates:
  - `sudo apt-get clean`
  - `sudo apt-get update`
  - `sudo apt-get upgrade`
  - `sudo apt-get dist-upgrade`
  - `sudo apt-get autoremove`
  - `sudo reboot`
  
2. Backup the database:
  - `cd ~`
  - `mysqldump --user=mnwebuser --password=******** mnwebdb > mnwebdb-yyyy-mm-dd.sql`
  
3. Backup the website media:
  - `cd /var/www/maneki-neko-web`
  - `sudo tar cfz mnwebmedia-yyyy-mm-dd.tgz media`
  - `sudo chown webmaster:webmaster mnwebmedia-yyyy-mm-dd.tgz`
  - `mv mnwebmedia-yyyy-mm-dd.tgz ~`