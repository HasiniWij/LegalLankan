#!/bin/bash
echo starting server

# here we just use npm to run the build
cd /home/root/legalLankanFrontend-app
echo building application...
sudo npm run build

# start the application with pm2
echo starting application...
sudo pm2 start npm -- run production
