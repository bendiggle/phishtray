#!/bin/sh
echo "---- Preparing FE ------"
cd frontend
#yarn install
yarn build

echo "---- Updating static files ------"
cd ..
python manage.py collectstatic --noinput

echo "---- Apply Migrations ------"
python manage.py migrate
