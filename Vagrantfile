# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  	config.vm.define "fubuntuone", primary: true do |fubuntuone|

		fubuntuone.vm.box = "bento/ubuntu-17.10"
  		fubuntuone.vm.hostname ="fubuntuone"
  		fubuntuone.vm.network "forwarded_port", guest: 8000, host: 9001,
    			auto_correct: true
  		fubuntuone.vm.network "forwarded_port", guest: 8080, host: 9002,
    			auto_correct: true  
  		fubuntuone.vm.network "forwarded_port", guest: 4004, host: 9003,
    			auto_correct: true
  		fubuntuone.vm.network "forwarded_port", guest: 4001, host: 9004,
    			auto_correct: true
  		fubuntuone.vm.network "forwarded_port", guest: 5001, host: 9005,
    			auto_correct: true
  		fubuntuone.vm.network "forwarded_port", guest: 9006, host: 9006,
    			auto_correct: true

		fubuntuone.vm.provision "shell", inline: <<-SHELL
			sudo apt-get update
			sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
			sudo apt-key fingerprint 0EBFCD88

			sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu zesty stable"

			sudo apt-get -y update
			sudo apt-get -y install docker-ce
			sudo apt-get -y install wget curl git python-pip
			sudo pip install virtualenv 
			sudo curl -O https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz
			sudo tar -xvf go1.9.1.linux-amd64.tar.gz
			sudo mv go /usr/local
			echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
			source ~/.bashrc
			go version 

			wget https://dist.ipfs.io/go-ipfs/v0.4.15/go-ipfs_v0.4.15_linux-amd64.tar.gz
			tar xvfz go-ipfs_v0.4.15_linux-amd64.tar.gz
			cd go-ipfs
			sudo ./install.sh
			ipfs init
			ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/9006

			wget https://sawtooth.hyperledger.org/docs/core/releases/1.0.1/app_developers_guide/sawtooth-default.yaml
			sudo service docker start
			
			sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
			sudo chmod +x /usr/local/bin/docker-compose
			echo "This is the docker compose version"
			sudo docker-compose --version
			sudo docker-compose -f sawtooth-default.yaml up -d
			
		SHELL

	end

  	config.vm.define "fubuntutwo", autostart: false do |fubuntutwo|

		f-ubuntutwo.vm.box = "bento/ubuntu-17.10"
  		fubuntutwo.vm.hostname ="fubuntutwo"
  		fubuntutwo.vm.network "forwarded_port", guest: 8000, host: 9001,
    			auto_correct: true
  		fubuntutwo.vm.network "forwarded_port", guest: 8080, host: 9002,
    			auto_correct: true  
  		fubuntutwo.vm.network "forwarded_port", guest: 4004, host: 9003,
    			auto_correct: true
	end

  	config.vm.define "fclientone", autostart: false do |fclientone|

		fclientone.vm.box = "alipne/alpine64"
  		fclientone.vm.hostname ="fclientone"
  		fclientone.vm.network "forwarded_port", guest: 8000, host: 9001,
    			auto_correct: true
  		fclientone.vm.network "forwarded_port", guest: 8080, host: 9002,
    			auto_correct: true  
  		fclientone.vm.network "forwarded_port", guest: 4004, host: 9003,
    			auto_correct: true
	end

end
