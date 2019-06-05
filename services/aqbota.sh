#!/usr/bin/env bash

#bash -c "script /dev/null"
bash -c "source ~/.bashrc"
bash -c "cd ~/catkin_ws/"
bash -c "/opt/ros/kinetic/setup.sh"
bash -c "/home/robot/linorobot_ws/devel/setup.sh"
bash -c "export LINOLIDAR=rplidar"
bash -c "export LINOBASE=2wd"
bash -c "/opt/ros/kinetic/bin/catkin_make"
bash -c "roslaunch linorobot aqbota.launch"
#bash -c "script /dev/null"
#bash -c "screen roslaunch linorobot aqbota.launch"
