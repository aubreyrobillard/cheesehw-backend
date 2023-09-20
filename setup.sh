#!/usr/bin/env bash

# exit on error
set -o errexit

# install dependencies
pip3 install -r dependecies.txt

# run migrations in case any migrations hadn't been run yet
python3 manage.py migrate