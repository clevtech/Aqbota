#!/usr/bin/env bash

cp ./aqbota.sh /home/robot/aqbota.sh
sudo chmod 777 /home/robot/aqbota.sh
echo "Aqbota script is created"

cp ./aqbota.service /lib/systemd/system/aqbota.service
echo "Aqbota service is created"

sudo service aqbota start
echo "Aqbota service is started"
sudo service aqbota enable

echo "Aqbota is installed"

cp ./man-flask.sh /home/robot/man-flask.sh
sudo chmod 777 /home/robot/man-flask.sh
echo "Man flask script is created"

cp ./manual.service /lib/systemd/system/manual.service
echo "Man flask service is created"

sudo service manual start
echo "Man flask service is started"
sudo service manual enable

echo "DONE"