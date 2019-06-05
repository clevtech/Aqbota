#include <Arduino.h>

void setup() {
  // LED pins
  Serial.begin(115200); // Open serial monitor at 115200 baud to see ping results.
}

void loop()
{
  if (Serial.available() > 0) {
    int Value = Serial.read();
    Serial.println(Value + 1);
    }
}
