#!/usr/bin/env bash

cp ./aqbota.service /lib/systemd/system/aqbota.service
cp ./aqbota.sh /home/robot/aqbota.sh
sudo chmod 777 /home/robot/aqbota.sh

sudo service aqbota start
sudo service aqbota enable

echo "Aqbota is installed"