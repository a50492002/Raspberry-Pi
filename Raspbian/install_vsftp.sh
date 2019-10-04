sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install vsftpd -y
sudo mkdir /var/ftp
sudo chmod 777 /var/ftp
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.backup
sudo sed -i 's/#write_enable=YES/write_enable=YES/g' /etc/vsftpd.conf
sudo sed -i '$a local_root=/var/ftp/' /etc/vsftpd.conf
sudo sed -i '$a user_config_dir=/etc/vsftpd/userconfig' /etc/vsftpd.conf
sudo sed -i '$a force_dot_files=YES' /etc/vsftpd.conf
sudo sed -i '$a pasv_min_port=50000' /etc/vsftpd.conf
sudo sed -i '$a pasv_max_port=55000' /etc/vsftpd.conf
sudo mkdir /etc/vsftpd
sudo mkdir /etc/vsftpd/userconfig
sudo systemctl restart vsftpd
