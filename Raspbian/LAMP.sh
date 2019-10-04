sudo apt-get update -y
sudo apt-get upgrade -y

#install LAMP
sudo apt-get install -y apache2
sudo apt-get install -y mariadb-server mariadb-client
sudo apt-get install -y php php-cgi libapache2-mod-php php-common php-pear php-mbstring php-mysql
#sudo a2enconf php7.2-cgi
sudo a2enconf php7.3-cgi
sudo systemctl reload apache2
sudo apt-get install -y phpmyadmin php-mbstring php-gettext
