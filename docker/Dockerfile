FROM ubuntu:20.04

MAINTAINER Benjamin Kreilinger  <kreili11@ads.uni-passau.de>
MAINTAINER Luca Escher <escher06@ads.uni-passau.de>

RUN apt-get update -qq && apt-get install -qq \
	nano \
	vim \
	python3 \
	python3-pip

RUN useradd -m -G sudo -s /bin/bash duck && echo "duck:duck" | chpasswd
RUN usermod -a -G staff duck
USER duck
WORKDIR /home/duck

ADD --chown=duck:duck data data/

RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib

# If we use hdf5
#RUN pip install h5py
#RUN Rscript -e "install.packages('BiocManager')"
#RUN Rscript -e "BiocManager::install('rhdf5')"
