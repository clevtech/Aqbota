#!/usr/bin/env bash

bash -c "source /opt/ros/kinetic/setup.bash"
bash -c "source ~/catkin_ws/devel/setup.bash"
bash -c "source /home/robot/linorobot_ws/devel/setup.bash"
bash -c "catkin_make"
bash -c "roslaunch linorobot aqbota.launch"
