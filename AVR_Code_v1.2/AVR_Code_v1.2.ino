//////////////////////////////////////////////////////////
//  © XeRi-Coin Community 2021
//  Distributed under MIT License
//////////////////////////////////////////////////////////
//  https://github.com/XeRi-PL
//  https://adamstefaniak57.wixsite.com/xeri-avr-mining?lang=en - Official Website
//////////////////////////////////////////////////////////
//  If you don't know what to do, visit official website
//  and navigate to Getting Started page. Happy mining!
//////////////////////////////////////////////////////////


#include <Arduino.h>
#include "Hash.h"

void setup() {
  Serial.begin(115200);
}
delay(5000);
void loop() {

  // usage as String
  // SHA1:a9993e364706816aba3e25717850c26c9cd0d89d

  Serial.print("SHA1:");
  Serial.println(sha1("abc"));

  // usage as ptr
  // SHA1:a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
  uint8_t hash[20];
  sha1("test", &hash[0]);

  Serial.print("SHA1:");
  for (uint16_t i = 0; i < 20; i++) {
    Serial.print(hash[i]);
  }
  Serial.println();

  delay(1000);
}
