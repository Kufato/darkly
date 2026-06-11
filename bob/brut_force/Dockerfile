FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y \
    hydra \
    nmap \
    curl \
    wget \
    wordlists \
    iproute2 \
    iputils-ping \
    net-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN gunzip /usr/share/wordlists/rockyou.txt.gz

WORKDIR /root
CMD ["/bin/bash"]
