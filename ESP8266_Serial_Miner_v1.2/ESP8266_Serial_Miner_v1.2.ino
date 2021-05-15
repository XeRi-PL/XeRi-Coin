#include <ESP8266WiFi.h> // Include WiFi library
#include <ESP8266mDNS.h> // OTA libraries
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include "Hash.h"

void setup() {
  Serial.begin(115200); // Start serial connection
  Serial.println("\nXeRi-Coin ESP8266 Miner Beta v1.2");

  delay(rand() % 1000); // delay up to 1sec to stagger start-ups
  pinMode(LED_BUILTIN, OUTPUT); // prepare for blink() function

}

void loop() {
  Serial.println("Hello , Happy Mining !");
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
