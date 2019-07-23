#if (ARDUINO >= 100)
    #include <Arduino.h>
#else
    #include <WProgram.h>
#endif

#include <Servo.h>

#include "ros.h"
#include "ros/time.h"
//header file for publishing velocities for odom
#include "lino_msgs/Velocities.h"
//header file for cmd_subscribing to "cmd_vel"
#include "geometry_msgs/Twist.h"
//header file for pid server
#include "lino_msgs/PID.h"
//header file for imu
#include "lino_msgs/Imu.h"

#include "lino_base_config.h"
#include "Motor.h"
#include "Kinematics.h"
#include "PID.h"
#include "Imu.h"

// #define ENCODER_OPTIMIZE_INTERRUPTS // comment this out on Non-Teensy boards
#include "Encoder.h"

#define IMU_PUBLISH_RATE 20 //hz
#define COMMAND_RATE 20 //hz
#define DEBUG_RATE 5

float g_req_linear_vel_x = 0;
float g_req_linear_vel_y = 0;
float g_req_angular_vel_z = 0;

unsigned long g_prev_command_time = 0;

//callback function prototypes
void commandCallback(const geometry_msgs::Twist& cmd_msg);


ros::NodeHandle nh;

ros::Subscriber<geometry_msgs::Twist> cmd_sub("cmd_vel", commandCallback);

lino_msgs::Velocities raw_vel_msg;
ros::Publisher raw_vel_pub("raw_vel", &raw_vel_msg);

void setup()
{
    nh.initNode();
    nh.getHardware()->setBaud(57600);
    nh.subscribe(cmd_sub);
    nh.advertise(raw_vel_pub);

    while (!nh.connected())
    {
        nh.spinOnce();
    }
    nh.loginfo("LINOBASE CONNECTED");
    delay(1);
}

void loop()
{
    static unsigned long prev_control_time = 0;

    //this block drives the robot based on defined rate
    if ((millis() - prev_control_time) >= (1000 / COMMAND_RATE))
    {
        moveBase();
        prev_control_time = millis();
    }

    //this block stops the motor when no command is received
    if ((millis() - g_prev_command_time) >= 400)
    {
        stopBase();
        moveBase();
    }
    //call all the callbacks waiting to be called
    nh.spinOnce();
}


void commandCallback(const geometry_msgs::Twist& cmd_msg)
{
    g_req_linear_vel_x = roundit(cmd_msg.linear.x);
    g_req_linear_vel_y = roundit(cmd_msg.linear.y);
    g_req_angular_vel_z = roundit(cmd_msg.angular.z);
    g_prev_command_time = millis();

}

int roundit(float val){
  int out = 0;
  if(val>=0.5){
    out = 1;
  }
  if(val<=-0.5){
    out = -1;
  }
  return out;
}

float angular(int x, int y){
  float ang = ((y-x)/2)/(0.64);
  return ang;
}

void moveBase()
{
    //pass velocities to publisher object
    raw_vel_msg.linear_x = g_req_linear_vel_x;
    raw_vel_msg.linear_y = g_req_linear_vel_y;
    raw_vel_msg.angular_z = angular(g_req_linear_vel_x, g_req_linear_vel_y);

    //publish raw_vel_msg
    raw_vel_pub.publish(&raw_vel_msg);
}

void stopBase()
{
    g_req_linear_vel_x = 0;
    g_req_linear_vel_y = 0;
    g_req_angular_vel_z = 0;
}
