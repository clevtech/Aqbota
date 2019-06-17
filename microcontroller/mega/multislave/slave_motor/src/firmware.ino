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

ros::NodeHandle nh;

Controller motor1_controller(Controller::MOTOR_DRIVER, MOTOR1_PWM, MOTOR1_IN_A, MOTOR1_IN_B);
Controller motor2_controller(Controller::MOTOR_DRIVER, MOTOR2_PWM, MOTOR2_IN_A, MOTOR2_IN_B);

float g_req_linear_vel_x = 0;
float g_req_linear_vel_y = 0;
float g_req_angular_vel_z = 0;

int RPM1 = 0;
int RPM2 = 0;

unsigned long g_prev_command_time = 0;

//callback function prototypes
void commandCallback(const geometry_msgs::Twist& cmd_msg);


ros::Subscriber<geometry_msgs::Twist> cmd_sub("cmd_vel", commandCallback);


void setup()
{

  stopBase();

    nh.initNode();
    nh.getHardware()->setBaud(57600);
    nh.subscribe(cmd_sub);

    while (!nh.connected())
    {
        stopBaseInit();
        nh.spinOnce();
    }
    nh.loginfo("MOTOR CONTROLLER IS CONNECTED");
    delay(1);
}

void loop()
{
      static unsigned long prev_control_time = 0;
      static unsigned long prev_debug_time = 0;

    //this block drives the robot based on defined rate
    if ((millis() - prev_control_time) >= (1000 / COMMAND_RATE))
    {
        moveBase();
        prev_control_time = millis();
    }

    //this block stops the motor when no command is received
    if ((millis() - g_prev_command_time) >= 400)
    {
        stopBaseInit();
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

void KinectRelay()
{
      if (g_req_linear_vel_x == 1){
        if (g_req_angular_vel_z == 0) {
          RPM1 = 10;
          RPM2 = 10;
        }
        if (g_req_angular_vel_z == -1) {
          RPM1 = 10;
          RPM2 = 0;
        }
        if (g_req_angular_vel_z == 1) {
          RPM1 = 0;
          RPM2 = 10;
        }
      }
      else if (g_req_linear_vel_x == -1){
        if (g_req_angular_vel_z == 0) {
          RPM1 = -10;
          RPM2 = -10;
        }
        if (g_req_angular_vel_z == -1) {
          RPM1 = 0;
          RPM2 = -10;
        }
        if (g_req_angular_vel_z == 1) {
          RPM1 = -10;
          RPM2 = 0;
        }
      }
      else if (g_req_linear_vel_x == 0){
        if (g_req_angular_vel_z == 0) {
          RPM1 = 0;
          RPM2 = 0;
        }
        if (g_req_angular_vel_z == -1) {
          RPM1 = 10;
          RPM2 = -10;
        }
        if (g_req_angular_vel_z == 1) {
          RPM1 = -10;
          RPM2 = 10;
        }
      }
}


void moveBase()
{
    KinectRelay();
    // printPWM1(RPM1);
    // printPWM2(RPM2);
    motor1_controller.spin(RPM1);
    motor2_controller.spin(RPM2);
}


void stopBaseInit(){
  motor1_controller.spin(0);
  motor2_controller.spin(0);
  g_req_linear_vel_x = 0;
  g_req_linear_vel_y = 0;
  g_req_angular_vel_z = 0;
}


void stopBase()
{
    motor1_controller.spin(0);
    motor2_controller.spin(0);
    g_req_linear_vel_x = 0;
    g_req_linear_vel_y = 0;
    g_req_angular_vel_z = 0;

}


void printPWM1(long val)
{
    char buffer[50];

    sprintf (buffer, "Motor 1 is  : %ld", val);
    nh.loginfo(buffer);
}

void printPWM2(long val)
{
    char buffer[50];

    sprintf (buffer, "Motor 2 is  : %ld", val);
    nh.loginfo(buffer);
}
