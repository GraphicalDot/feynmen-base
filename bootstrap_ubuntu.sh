
#!/usr/bin/env bash

## Update sources 

sudo apt-get update -y
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common





sudo apt-get -y install wget curl git python-pip
sudo pip install virtualenv 


##installing go
sudo curl -O https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz
sudo tar -xvf go1.9.1.linux-amd64.tar.gz
sudo mv go /usr/local
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
source ~/.bashrc
go version 


## Installing IPFs and configuration of IPFS
wget https://dist.ipfs.io/go-ipfs/v0.4.15/go-ipfs_v0.4.15_linux-amd64.tar.gz
tar xvfz go-ipfs_v0.4.15_linux-amd64.tar.gz
cd go-ipfs
sudo ./install.sh
sudo apt-get -y install fuse 
sudo groupadd fuse
sudo usermod -aG fuse $(whoami)

ipfs init
ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/9006



##Installing Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu zesty stable"
sudo apt-get -y update
sudo apt-get -y install docker-ce
sudo service docker start

##installing docker compose 
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
echo "This is the docker compose version"
sudo docker-compose --version


##installing sawtooth-core, and bringing up hyperledger sawtooth docker containers
wget https://sawtooth.hyperledger.org/docs/core/releases/1.0.1/app_developers_guide/sawtooth-default.yaml
			
sudo docker-compose -f sawtooth-default.yaml up -d
			

