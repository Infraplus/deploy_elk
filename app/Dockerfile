FROM ubuntu:20.04

MAINTAINER Iurie Muradu iurie.muradu@weazel.fr

RUN apt update && \
    apt install python3-pip vim curl -y && \
    pip3 install Flask
    
RUN useradd -ms /bin/bash salmen -u 666 -U 

COPY helloworld.py /home/salmen

RUN mkdir /home/salmen/logs
RUN chmod +x /home/salmen/helloworld.py && chown -R salmen:salmen /home/salmen

EXPOSE 5000

USER salmen
WORKDIR /home/salmen

CMD ./helloworld.py
