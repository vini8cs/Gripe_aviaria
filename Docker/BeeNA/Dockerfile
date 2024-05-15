
FROM ubuntu:22.04
WORKDIR /app-beena
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get update
#decrease the image size by removing the contents of the /var/lib/apt/lists/ directory
RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/* 
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh


