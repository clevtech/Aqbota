#include <Arduino.h>
#define interval 1000

void setup() {
  int incomingByte = 0;
  int ledPins2[] = {7, 8, 9, 10}; // LED pins
   // Open serial monitor at 115200 baud to see ping results.
  for(int p=0; p<4; p++)
   {
       pinMode(ledPins2[p], OUTPUT); // Set the mode to OUTPUT
       digitalWrite(ledPins2[p], HIGH);
   }
  Serial.begin(115200);
}

void loop()
{
  if (Serial.available() > 0) {
    int Value = Serial.read();
    if (Value == 63){
      Serial.println("Box");
    }
    else{
        int incomingByte = Value - 48;
        int ledPins[] = {7, 8, 9, 10};
        Serial.println(ledPins[incomingByte]);
        digitalWrite(ledPins[incomingByte], LOW);
        delay(interval);
        digitalWrite(ledPins[incomingByte], HIGH);
  }
        }
}
