#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

if __name__ == "__main__":
    os.system("catkin_make")
    os.system("source /home/robot/linorobot_ws/devel/setup.bash")
    os.system("roslaunch linorobot aqbota.launch")
    print("OK!")
