FROM ubuntu:20.04

MAINTAINER Benjamin Kreilinger <kreili11@ads.uni-passau.de>
MAINTAINER Luca Escher <escher06@ads.uni-passau.de>

RUN apt-get update -qq 
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/CET apt-get -y install tzdata
RUN apt-get -y install \
	nano \
	vim \
	python3 \
	python3-pip \
#	latexmk
	texlive-latex-base \
	texlive-pictures \
	texlive-science \
	texlive-latex-extra

RUN useradd -m -G sudo -s /bin/bash duck && echo "duck:duck" | chpasswd
RUN usermod -a -G staff duck
USER duck
WORKDIR /home/duck

RUN pip3 install -U kaleido
RUN pip3 install pandas
RUN pip3 install plotly
RUN pip3 install pulp