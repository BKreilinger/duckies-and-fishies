#!/bin/bash

python3 ../generate_product_mixes_graphs.py

is_arm=$(uname -a)

if [[ $is_arm =~ .*x86_64.*  ]]; then
	python3 ../
	# todo: execute solver

	# todo generate latex file
fi

