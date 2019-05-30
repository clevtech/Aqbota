#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Bauyrzhan Ospan"
__copyright__ = "Copyright 2018, KazPostBot"
__version__ = "1.0.1"
__maintainer__ = "Bauyrzhan Ospan"
__email__ = "bospan@cleverest.tech"
__status__ = "Development"

from __future__ import print_function

import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty
from flask import Flask, render_template, request, Markup, jsonify


app = Flask(__name__)  # Creating new flask app
settings, pub, speed, turn, x, y, z, th, status, moveBindings = init_motion()

def init_motion():
    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('teleop_twist_keyboard')

    speed = rospy.get_param("~speed", 0.5)
    turn = rospy.get_param("~turn", 1.0)
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    moveBindings = {
        'i': (1, 0, 0, 0),
        'o': (1, 0, 0, -1),
        'j': (0, 0, 0, 1),
        'l': (0, 0, 0, -1),
        'u': (1, 0, 0, 1),
        ',': (-1, 0, 0, 0),
        '.': (-1, 0, 0, 1),
        'm': (-1, 0, 0, -1),
        'O': (1, -1, 0, 0),
        'I': (1, 0, 0, 0),
        'J': (0, 1, 0, 0),
        'L': (0, -1, 0, 0),
        'U': (1, 1, 0, 0),
        '<': (-1, 0, 0, 0),
        '>': (-1, -1, 0, 0),
        'M': (-1, 1, 0, 0),
        't': (0, 0, 1, 0),
        'b': (0, 0, -1, 0),
    }

    return settings, pub, speed, turn, x, y, z, th, status, moveBindings


def motion(key):
    print(key)
    try:
        if key in moveBindings.keys():
            x = moveBindings[key][0]
            y = moveBindings[key][1]
            z = moveBindings[key][2]
            th = moveBindings[key][3]
        elif key in speedBindings.keys():
            speed = speed * speedBindings[key][0]
            turn = turn * speedBindings[key][1]
            status = (status + 1) % 15
        else:
            x = 0
            y = 0
            z = 0
            th = 0
            if (key == '\x03'):
                break

        twist = Twist()
        twist.linear.x = x * speed;
        twist.linear.y = y * speed;
        twist.linear.z = z * speed;
        twist.angular.x = 0;
        twist.angular.y = 0;
        twist.angular.z = th * turn
        pub.publish(twist)

    except Exception as e:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0;
        twist.linear.y = 0;
        twist.linear.z = 0
        twist.angular.x = 0;
        twist.angular.y = 0;
        twist.angular.z = 0
        pub.publish(twist)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


@app.route('/robot-control/')
def robcont():
    return render_template("control.html")


@app.route('/robot-control/<direction>', methods=['POST'])
def ajax_request(direction):
    print(str(direction))
    direction = str(direction).replace("\n", '').replace("\r", '').replace("/", "")
    if direction == "<":
        motion(",")
    elif direction == ">":
        motion(".")
    else:
        motion(direction)
    return jsonify()


# Main flask app
if __name__ == "__main__":
    app.run("0.0.0.0", port=7777, debug=True)
