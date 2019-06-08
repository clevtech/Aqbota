#include "Motor.h"

Controller::Controller(driver motor_driver, int pwm_pin, int motor_pinA, int motor_pinB):
    motor_driver_(motor_driver),
    pwm_pin_(pwm_pin),
    motor_pinA_(motor_pinA),
    motor_pinB_(motor_pinB)
{
    switch (motor_driver)
    {
        case L298:
            pinMode(motor_pinA_, OUTPUT);
            pinMode(motor_pinB_, OUTPUT);
            digitalWrite(motor_pinA_, LOW);
            digitalWrite(motor_pinB_, LOW);
            break;
    }
}

void Controller::spin(int pwm)
{
    switch (motor_driver_)
    {
        case L298:
            if(pwm > 0)
            {
                digitalWrite(motor_pinA_, HIGH);
                digitalWrite(motor_pinB_, LOW);
            }
            else
            {
              if(pwm < 0)
                {
                  digitalWrite(motor_pinA_, LOW);
                  digitalWrite(motor_pinB_, HIGH);
                }
              else {
                digitalWrite(motor_pinA_, LOW);
                digitalWrite(motor_pinB_, LOW);
                }
            }
            break;
    }
}
