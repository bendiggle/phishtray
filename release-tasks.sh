#!/bin/sh
ls
echo "----------"
cd frontend
pwd
echo "---- INSTALL ------"
npm install
echo "---- BUILD ------"
npm run build
