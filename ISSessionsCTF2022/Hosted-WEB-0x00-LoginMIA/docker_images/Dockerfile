FROM php:7.2-apache

COPY index.php /var/www/html/index.php
COPY flag.php /var/www/html/flag.php

EXPOSE 8000

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]