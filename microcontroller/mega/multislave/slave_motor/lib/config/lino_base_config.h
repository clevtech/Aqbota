#ifndef LINO_BASE_CONFIG_H
#define LINO_BASE_CONFIG_H

//uncomment the base you're building
#define LINO_BASE DIFFERENTIAL_DRIVE // 2WD and Tracked robot w/ 2 motors

//uncomment the motor driver you're using
#define USE_L298_DRIVER

//uncomment the IMU you're using
#define USE_GY85_IMU

#define DEBUG 1

#define K_P 0 // P constant
#define K_I 0 // I constant
#define K_D 0 // D constant

//define your robot' specs here
#define MAX_RPM 330               // motor's maximum RPM
#define COUNTS_PER_REV 1550       // wheel encoder's no of ticks per rev
#define WHEEL_DIAMETER 0.10       // wheel's diameter in meters
#define PWM_BITS 1                // PWM Resolution of the microcontroller
#define LR_WHEELS_DISTANCE 0.235  // distance between left and right wheels
#define FR_WHEELS_DISTANCE 0.30   // distance between front and rear wheels. Ignore this if you're on 2WD/ACKERMANN
#define MAX_STEERING_ANGLE 0.415  // max steering angle. This only applies to Ackermann steering

// ENCODER PINS
#define MOTOR1_ENCODER_A 2  //Int0 Pin 2
#define MOTOR1_ENCODER_B 3  //Int1 Pin 3

#define MOTOR2_ENCODER_A 18 //Int2 Pin 18
#define MOTOR2_ENCODER_B 19 //Int3 Pin 19


//MOTOR PINS

#define MOTOR_DRIVER L298

#define MOTOR1_PWM 13


#define MOTOR2_PWM 4


#define STEERING_PIN 9

#define PWM_MAX 1
#define PWM_MIN -PWM_MAX

#define MOTOR1_IN_A 5
#define MOTOR1_IN_B 6
#define MOTOR2_IN_A 7
#define MOTOR2_IN_B 8

#endif
