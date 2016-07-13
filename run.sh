#!/bin/bash

cd static
#grunt quickly
#grunt build --force
grunt build
cd ..
python3 manage.py test
python3 manage.py runserver
