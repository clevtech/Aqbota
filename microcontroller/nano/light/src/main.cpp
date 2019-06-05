#include <Arduino.h>
#define interval 1000

void setup() {
  int ledPins2[] = {13};
  for(int p=0; p<1; p++)
   {
       pinMode(ledPins2[p], OUTPUT);
   }
  int incomingByte = 0;
  // LED pins
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
}

void loop()
{
  if (Serial.available() > 0) {
    int Value = Serial.read();
    if (Value == 63){
      Serial.println("Light");
    }
    else if(Value == 48){
      Serial.println("OFF");
      digitalWrite(13, HIGH);
    }
    else{
      Serial.println("ON");
      digitalWrite(13, LOW);
  }
        }
}
