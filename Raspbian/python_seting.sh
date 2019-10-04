sudo apt-get update -y
sudo apt-get upgrade -y

#install pip3
sudo apt-get install python3-pip -y
pip3 install --upgrade pip
sudo sed -i '$a # Add this line inside ~/.bash_profile:' ~/.bashrc
sudo sed -i '$a export PATH=$PATH:~/.local/bin' ~/.bashrc
source ~/.bashrc
sudo apt-get install libatlas-base-dev

pip3 install jupyter --user
jupyter notebook --generate-config
jupyter notebook password
jupyter notebook --ip=0.0.0.0 --port=8888
