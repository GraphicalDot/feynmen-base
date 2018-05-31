
#!/bin/bash 

#https://stackoverflow.com/questions/20845056/how-can-i-expose-more-than-1-port-with-docker
#sudo docker build -t registry.gitlab.com/mesha/feynmen/feynmen_dnode:protoype -f DockerFiles/Dockerfile . 
sudo docker build -t feynmen_dnode:v1.0 -f DockerFiles/Dockerfile . 



#docker run -d --name feynmen_dnode \
#	  -v /tmp/ipfs-docker-staging:/export -v /tmp/ipfs-docker-data:/data/ipfs \
#	    -p 8080:8080 -p 4001:4001 -p 127.0.0.1:5001:5001 feynmen:prototype

