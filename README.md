# feynmen-base
This is the base implementation for hyperledger sawtooth and IPFS.
For installation:
	In the fabfile.py change the env.hosts config for the IP of the VM or Remote machine.
		And also enter the respective ssh key for the machine.
	If you are using vagrant, then use the VagrantFile for booting vagrant VM.
		vagrant up fubuntuone
	TO see, Location of its ssh key use
		vagrant ssh_config fubuntuone
	This will show you the location os ssh file, copy the location of that key in the 
	fabfile.py

	Use fab -H  deploy localhost

	This will get the Vagrant VM up and running with necessary cofigurations.

Note: 
	Sometimes the remote URL's for downloading packaged wont work. Dont panic and wait for sometime.

UserInterface: 
	Kivy Desktop application, For username and password:
		Username: admin
		Password: 1234
		Right now, the API have not been integrated. The app will create a feynmen.json file in the UserInterface
		Folder which stores the SHA3_256 hash of the password and username.

