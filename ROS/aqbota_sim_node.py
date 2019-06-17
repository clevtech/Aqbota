#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from sensor_msgs.msg import Imu
import tf
from sensor_msgs.msg import NavSatFix
import math
from math import sin, cos, pi


def imu_callback(data):
    global w
    w = data.orientation.z
    rospy.loginfo("Orient is: %s", data.orientation.z)


def callback(data):
    global last_time
    global w
    global x
    global y
    global A

    global timer
    try:
        timer.shutdown()
    except:
        pass

    # rospy.loginfo(rospy.get_caller_id() + "cmd_vel x is: %s", data.linear.x)
    # rospy.loginfo(rospy.get_caller_id() + "cmd_vel z is: %s", data.angular.z)

    if w is not None and x is not None and y is not None:
        current_time = rospy.Time.now()
        if last_time is None:
            last_time = rospy.Time.now()

        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"

        dt = (current_time - last_time).to_sec()

        delta_x = (A * data.linear.x * cos(w)) * dt
        delta_y = (A * data.linear.x * sin(w)) * dt

        x += delta_x
        y += delta_y

        odom_quat = tf.transformations.quaternion_from_euler(0, 0, w)

        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(A*data.linear.x, 0, 0), Vector3(0, 0, w))

        timer = rospy.Timer(rospy.Duration(0.4), my_callback)
        # publish the message
        global odom_pub
        odom_pub.publish(odom)
        last_time = current_time


def my_callback(event):
    rospy.loginfo("TIMER!!!!")
    global w
    global x
    global y
    try:
        current_time = rospy.Time.now()
        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, w)

        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(0, 0, 0), Vector3(0, 0, w))
        # publish the message
        global odom_pub
        odom_pub.publish(odom)
        last_time = current_time
    except:
        pass

def listener():
    rospy.init_node('new_odom')
    global odom_pub
    odom_pub = rospy.Publisher("raw_odom2", Odometry, queue_size=50)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.Subscriber("/android/imu", Imu, imu_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    global w
    global A
    global x
    global y
    global last_time
    last_time = None
    x, y = 0, 0
    A = 1
    w = None
    global timer
    timer = None
    listener()

