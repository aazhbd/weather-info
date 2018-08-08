#!/bin/dash
virtualenv -q -p python3 renv $1
source ./renv/bin/activate
pip install -r requirements.txt

