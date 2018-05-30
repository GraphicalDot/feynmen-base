FROM ubuntu:latest
#WORKDIR /root

RUN apt-get update && apt-get install apt-utils curl -y


RUN curl -s https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz | tar -v -C /usr/local -xz
ENV PATH $PATH:/usr/local/go/bin


ENV GOROOT=/usr/lib/go \
	GOPATH=$HOME/go \
	PATH=$PATH:$GOROOT/bin:$GOPATH/bin

RUN curl https://dist.ipfs.io/go-ipfs/v0.4.15/go-ipfs_v0.4.15_linux-amd64.tar.gz | tar xz
WORKDIR go-ipfs
RUN  bash install.sh && rm -rf * 





EXPOSE 4001 4002/udp 5001 8080 8081 9001



ENV IPFS_PATH /data/ipfs
RUN mkdir -p $IPFS_PATH \
  && useradd -s /usr/sbin/nologin -d $IPFS_PATH -u 1000 -G users ipfs \
  && chown ipfs:users $IPFS_PATH

# Expose the fs-repo as a volume.
# start_ipfs initializes an fs-repo if none is mounted.
VOLUME $IPFS_PATH
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#ENTRYPOINT ["/usr/local/bin/ipfs"]

##docker build --build-arg SSH_KEY_FILE =~/.ssh/id_rsa -f Dockerfile .
#ipfs init && ipfs daemon &&\
#	ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/9001 && \
#	ipfs config Addresses.API /ip4/0.0.0.0/tcp/5001 && \
#	ipfs config --json Experimental.FilestoreEnabled true

