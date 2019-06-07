#include <Arduino.h>
#define interval 1000

void setup() {
  int incomingByte = 0;
  int ledPins2[5] = {7, 8, 9, 10, 4}; // LED pins
   // Open serial monitor at 115200 baud to see ping results.
  for(int p=0; p<5; p++)
   {
       pinMode(ledPins2[p], OUTPUT); // Set the mode to OUTPUT
       digitalWrite(ledPins2[p], HIGH);
   }
  Serial.begin(115200);
}

void loop()
{
  int ledPins[4] = {7, 8, 9, 10};
  if (Serial.available() > 0) {
    int Value = Serial.read();
    int incomingByte = Value - 48;
    if(incomingByte == 4){
      digitalWrite(4, HIGH);
    }
    else if(incomingByte == 5){
      digitalWrite(4, LOW);
    }
    else{
    digitalWrite(ledPins[incomingByte], LOW);
    delay(interval);
    digitalWrite(ledPins[incomingByte], HIGH);
  }
  Serial.println(incomingByte);
}
}
