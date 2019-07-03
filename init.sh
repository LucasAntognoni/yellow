#!/bin/bash

echo "\n\nInstalling dependencies...\n\n"
pip3 install --upgrade pipenv
pipenv install --deploy --system

echo "\n\nDowloading catalog from Google Cloud Storage\n\n"
gsutil cp gs://catalog-store/catalog.csv bucket
