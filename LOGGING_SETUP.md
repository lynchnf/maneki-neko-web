Logging Setup
==============

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
