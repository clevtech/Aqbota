#!/usr/bin/env bash

cp ./aqbota.sh /home/robot/aqbota.py
sudo chmod 777 /home/robot/aqbota.py
echo "Aqbota script is created"

cp ./aqbota.service /lib/systemd/system/aqbota.service
echo "Aqbota service is created"

sudo service aqbota start
echo "Aqbota service is started"
sudo service aqbota enable

echo "Aqbota is installed"