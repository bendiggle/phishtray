#!/bin/sh
echo "---- Apply Migrations ------"
python manage.py migrate


echo "---- Check Static ------"
python manage.py findstatic


