FROM ubuntu:latest
#WORKDIR /root
#https://kivy.org/docs/installation/installation-linux.html
RUN apt-get update && apt-get install -y apt-utils curl \
    python-pip \
    build-essential \
    git \
    python \
    python-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev python3 python3-pip python3-setuptools



RUN pip3 install Cython==0.25.2
RUN pip3 install kivy
RUN garden install filebrowser
ADD UserInterface/ /feynmen-base
WORKDIR /feynmen-base

CMD ["python3", "main.py"]



RUN curl -s https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz | tar -v -C /usr/local -xz
ENV PATH $PATH:/usr/local/go/bin


ENV GOROOT=/usr/lib/go \
	GOPATH=$HOME/go \
	PATH=$PATH:$GOROOT/bin:$GOPATH/bin

RUN curl https://dist.ipfs.io/go-ipfs/v0.4.15/go-ipfs_v0.4.15_linux-amd64.tar.gz | tar xz
WORKDIR /go-ipfs
RUN  bash install.sh && rm -rf * 





EXPOSE 4001 4002/udp 5001 8080 8081 9001


ENV IPFS_PATH /data/ipfs
RUN mkdir -p $IPFS_PATH && mkdir /UserInterface\
  && useradd -s /usr/sbin/nologin -d $IPFS_PATH -u 1000 -G users ipfs \
  && chown ipfs:users $IPFS_PATH

# Expose the fs-repo as a volume.
# start_ipfs initializes an fs-repo if none is mounted.
VOLUME $IPFS_PATH
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#ENTRYPOINT ["/usr/local/bin/ipfs"]

ADD UserInterface/ /feynmen-base
##docker build --build-arg SSH_KEY_FILE =~/.ssh/id_rsa -f Dockerfile .
#ipfs init && ipfs daemon &&\
#	ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/9001 && \
#	ipfs config Addresses.API /ip4/0.0.0.0/tcp/5001 && \
#	ipfs config --json Experimental.FilestoreEnabled true

#docker run -it --name feynmen_prototype_container -p 5001:5001 -p 4001:4001 -p 9001:9001   -v ~/.docker_data/feynmen_protype:/data/ipfs fa8b4720d4c4 /bin/bash
#RUN - Install Python , your container now has python burnt into its image 
#CMD - python hello.py , run your favourite script, Only One CMD command execution will be respected.


