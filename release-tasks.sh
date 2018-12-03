#!/bin/sh
echo "---- Preparing FE ------"
cd frontend
yarn install
yarn build

echo "---- Updating static files ------"
python manage.py collectstatic --noinput

echo "---- Migrate ------"

