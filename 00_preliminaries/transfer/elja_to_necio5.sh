#!/bin/bash

# this is a command to transfer files from elja to necio5. Should be run in necio5. OK from IT on 2024.05.27

# rsync source target
# -e specifies a remote shell

rsync -azPvh --bwlimit=40000  -e "ssh -i ~/.ssh/elja" adrian@elja.hi.is:/hpcdata/Mimir/adrian/research/keilir/data/tempo /Users/adrian/tempo/.
