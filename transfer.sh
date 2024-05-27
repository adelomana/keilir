#!/bin/bash

# this is a command to transfer files from necio5 to elja. Should be run in necio5. OK from IT on 2024.05.27

rsync -azPvh --bwlimit=40000 /Users/adrian/research/keilir/data/raw_fastq -e "ssh -i ~/.ssh/elja" adrian@elja.hi.is:/hpcdata/Mimir/adrian/research/keilir/data
