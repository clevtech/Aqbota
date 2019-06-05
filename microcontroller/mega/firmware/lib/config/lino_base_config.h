#ifndef LINO_BASE_CONFIG_H
#define LINO_BASE_CONFIG_H

//uncomment the base you're building
#define LINO_BASE DIFFERENTIAL_DRIVE

//uncomment the motor driver you're using
#define USE_L298_DRIVER

//uncomment the IMU you're using
#define USE_GY85_IMU

#define DEBUG 1

#define K_P 0.6 // P constant
#define K_I 0.3 // I constant
#define K_D 0.5 // D constant

//define your robot' specs here
#define MAX_RPM 330               // motor's maximum RPM
#define COUNTS_PER_REV 1550       // wheel encoder's no of ticks per rev
#define WHEEL_DIAMETER 0.10       // wheel's diameter in meters
#define PWM_BITS 8                // PWM Resolution of the microcontroller
#define LR_WHEELS_DISTANCE 0.235  // distance between left and right wheels
#define FR_WHEELS_DISTANCE 0.30   // distance between front and rear wheels. Ignore this if you're on 2WD/ACKERMANN
#define MAX_STEERING_ANGLE 0.415  // max steering angle. This only applies to Ackermann steering

// ENCODER PINS
#define MOTOR1_ENCODER_A 16  //Int0 Pin 2
#define MOTOR1_ENCODER_B 17  //Int1 Pin 3

#define MOTOR2_ENCODER_A 18 //Int2 Pin 18
#define MOTOR2_ENCODER_B 19 //Int3 Pin 19

#define MOTOR3_ENCODER_A 30  //Placeholder (set to unused mega pin)
#define MOTOR3_ENCODER_B 31  //Placeholder (set to unused mega pin)

#define MOTOR4_ENCODER_A 32  //Placeholder (set to unused mega pin)
#define MOTOR4_ENCODER_B 33  //Placeholder (set to unused mega pin)

//MOTOR PINS

#define MOTOR_DRIVER L298

#define MOTOR1_PWM 4
#define MOTOR1_IN_A 44
#define MOTOR1_IN_B 45

#define MOTOR2_PWM 13
#define MOTOR2_IN_A 46
#define MOTOR2_IN_B 47

#define MOTOR3_PWM 36   //Placeholder (set to unused mega pin)
#define MOTOR3_IN_A 37  //Placeholder (set to unused mega pin)
#define MOTOR3_IN_B 38  //Placeholder (set to unused mega pin)

#define MOTOR4_PWM 39   //Placeholder (set to unused mega pin)
#define MOTOR4_IN_A 40  //Placeholder (set to unused mega pin)
#define MOTOR4_IN_B 41  //Placeholder (set to unused mega pin)

#define STEERING_PIN 7

#define PWM_MAX 255
#define PWM_MIN -PWM_MAX

#endif
