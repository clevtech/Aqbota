#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion

def imu_callback(data):
    rospy.loginfo(data.orientation.z)
   #do something with z

def imu_listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/android/imu", Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    imu_listener()

