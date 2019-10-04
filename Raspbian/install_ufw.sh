sudo apt-get update -y
sudo apt-get upgrade -y

sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 58888
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ftp
sudo ufw allow ftps
sudo ufw allow 50000:55000/tcp
sudo ufw enable
