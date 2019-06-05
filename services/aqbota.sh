#!/usr/bin/env bash

bash -c "cd catkin_ws && catkin_make && source /home/robot/catkin_ws/devel/setup.bash && roslaunch linorobot aqbota.launch"
