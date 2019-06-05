#!/usr/bin/env bash

bash -c "source /home/robot/catkin_ws/devel/setup.bash"
bash -c "catkin_make"
bash -c "roslaunch linorobot aqbota.launch"
