#!/bin/bash

python3 ./scripts/solver.py
pdflatex -output-directory ./data/documentation ./data/basedata/final_paper.tex

rm ./data/documentation/final_paper.log
rm ./data/documentation/final_paper.aux