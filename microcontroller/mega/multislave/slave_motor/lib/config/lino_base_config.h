#ifndef LINO_BASE_CONFIG_H
#define LINO_BASE_CONFIG_H

//uncomment the base you're building
#define LINO_BASE DIFFERENTIAL_DRIVE

//uncomment the motor driver you're using
#define USE_L298_DRIVER

//uncomment the IMU you're using
#define USE_GY85_IMU

#define DEBUG 1

#define K_P 0.3 // P constant
#define K_I 0.5 // I constant
#define K_D 0.7 // D constant

//define your robot' specs here
#define MAX_RPM 60                // motor's maximum RPM
#define COUNTS_PER_REV 241       // wheel encoder's no of ticks per rev
#define WHEEL_DIAMETER 0.34       // wheel's diameter in meters
#define PWM_BITS 8                // PWM Resolution of the microcontroller
#define LR_WHEELS_DISTANCE 0.65  // distance between left and right wheels
#define FR_WHEELS_DISTANCE 0.30   // distance between front and rear wheels. Ignore this if you're on 2WD/ACKERMANN
#define MAX_STEERING_ANGLE 0.415  // max steering angle. This only applies to Ackermann steering



//MOTOR PINS

#define MOTOR_DRIVER L298

#define MOTOR1_PWM 13

#define MOTOR1_IN_A 4
#define MOTOR1_IN_B 5

#define MOTOR2_PWM 33
#define MOTOR2_IN_A 6
#define MOTOR2_IN_B 7

#define PWM_MAX 50
#define PWM_MIN -PWM_MAX

#define STEERING_PIN 32


#endif
