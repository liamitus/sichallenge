#!/bin/bash

cd static
#grunt quickly
grunt build --force
cd ..
python3 manage.py runserver
