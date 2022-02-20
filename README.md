# Duckies and Fishies reproduction package

This project aims to reproduce the process of the "duckies and fishies project" from Micheal Milton,
[Head First Data Analysis](https://www.oreilly.com/library/view/head-first-data/9780596806224/).

This project was created within the scope of the lecture "Reproducibility Engineering" at the University of Passau and the University of Regensburg.

[![DOI](https://zenodo.org/badge/446453835.svg)](https://zenodo.org/badge/latestdoi/446453835)

## Content

* [Project setup](#project-setup)
* [Execution](#execution)
* [Results](#results)
* [Hardware and operating system](#hardware-and-operating-system)
* [Sources](#sources)
* [Team](#team)

## Project setup

1. Install [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) 

2. Clone the project

    Git:
        `git clone https://github.com/BKreilinger/duckies-and-fishies.git`
   
    Zenodo:
        `https://doi.org/10.5281/zenodo.6190165`

3. Execute start script

### On Linux and macOS


    ./start.sh
    optional parameters:
    -a  builds a second docker container which can run the linear programming calculations on arm architecture
    -n  force not building second container in case the problem is fixed in the future


### On Windows


    bash ./start.sh
    optional parameters:
    -a  builds a second docker container which can run the linear programming calculations on arm architecture
    -n  force not building second container in case the problem is fixed in the future
    

**Important!!**

If the problem with PuLP on arm doesn't exist anymore use: `./start.sh -n`
This forces not to build the second docker container even though the script detects you are using the arm architecture.


## Execution

### Automatic execution
All scripts are executed automatically when running *start.sh* script.

### Manual execution

#### Build and start docker container(s)

To build both containers (if you are on arm architecture):


    cd docker
    docker-compose up -d

To build only the "normal" container:


    cd docker
    docker-compose up -d ubuntu

To enter the bash of the containers:


    docker-compose exec ubuntu bash         # for "normal" container
    docker-compose exec ubuntu-arm bash     # for second container on arm


#### Execute python scripts

If you are in scripts folder:

`python3 solver.py` (executes solver.py file)

If you are in project folder:

`python3 ./scripts/solver.py` (executes solver.py file)

## Results

### Location graphs
`/data/images/:`
- product_mix.png
- hist_sales_graph

### Location CSV files
`/data/csv_result_documents/:`
- bathing_firends_res1.csv
- bathing_firends_res2_with_estimated_demands.csv

### Location final PDF
`data/documentation/:`
- final_paper.pdf

## Hardware and operating system
This project was developed and tested on the following devices:

* MacBook Air (M1, 2020)
  * Chip: Apple M1, arm architecture
  * RAM: 8 GB
  * macOS Monterey, version 12.1

* Custom Tower PC
  * Chip: Ryzen 7 3700X, x86 architecture (64 bit)
  * RAM: 32 GB, 3600 mHz
  * Linux Ubuntu, version 20.04.3 LTS

## Sources
* [Basedata](https://resources.oreilly.com/examples/9780596153946/-/blob/master/bathing_friends_unlimited.xls)
* [Historical sales data](https://resources.oreilly.com/examples/9780596153946/-/blob/master/historical_sales_data.xls)
* [Kaleido](https://pypi.org/project/kaleido/)
* [Micheal Milton, Head First Data Analysis, 75-109](https://www.oreilly.com/library/view/head-first-data/9780596806224/)
* [Pandas](https://pandas.pydata.org/docs/)
* [PdfLaTex](https://wiki.ubuntuusers.de/LaTeX/)
* [Plotly](https://plotly.com/python/)
* [PuLP](https://coin-or.github.io/pulp/)
* [PYPL PopularitY of Programming Language](https://pypl.github.io/PYPL.html)

## Team
* [Benjamin Kreilinger](https://github.com/BKreilinger) 
* [Luca Escher](https://github.com/LucaUniPassau)


