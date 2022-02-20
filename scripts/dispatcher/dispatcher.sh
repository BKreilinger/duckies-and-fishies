#!/bin/bash

echo "Starting execution"

python3 ./scripts/generate_product_mix_graph.py
python3 ./scripts/reproduce_historical_sales_data_diagram.py

architecture=$(uname -a)

if [[ $architecture =~ .*x86_64.*  ]]; then
	python3 ./scripts/solver.py
	pdflatex -output-directory ./data/documentation ./data/basedata/final_paper.tex

	rm ./data/documentation/final_paper.log
	rm ./data/documentation/final_paper.aux
fi

