#!/bin/bash

# before you start, brew install wget

git clone https://github.com/snizam001/greenPipes

conda activate base

mamba env create --name keilir -f environment.keilir.yaml

conda activate keilir

cd greenPipes
chmod -R +x $(pwd)/greenPipes/*
pip install $(pwd)/

curl http://homer.ucsd.edu/homer/configureHomer.pl > tempo.pl
mv tempo.pl /Users/adrian/miniforge3/envs/keilir/bin/configureHomer.pl
perl /Users/adrian/miniforge3/envs/keilir/bin/configureHomer.pl -install hg38

cd -
