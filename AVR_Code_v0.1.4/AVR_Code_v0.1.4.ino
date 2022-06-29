//////////////////////////////////////////////////////////
//  © XeRi-Coin Community 2022
//  Distributed under MIT License
//////////////////////////////////////////////////////////
//  https://github.com/XeRi-PL
//
//////////////////////////////////////////////////////////
//  If you don't know what to do, visit official website
//  and navigate to Getting Started page. Happy mining!
//////////////////////////////////////////////////////////
#pragma GCC optimize ("-O0")
#include <Arduino.h>
#include "Hash.h"
#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif
#if defined(ARDUINO_ARCH_AVR) || defined(ARDUINO_ARCH_MEGAAVR)
typedef uint16_t uintDiff;
#else
typedef uint32_t uintDiff;
#endif

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  
  delay(100);
  while (!Serial) ;
    Serial.flush();
}
void minersetup()
{
}

void loop(void) {
  miner();
}
void miner() {
  delay (10);
  double MM = 0.00000001;
  do
  {
  //uint8_t hash[10];
  //sha1("test", &hash[0]);
  //Serial.print("SHA1:");
  //for (uint16_t i = 0; i < 10; i++) { Serial.print(hash[i]); }

    minersetup();
    
    #if defined(ARDUINO_ARCH_AVR)
    delay(100);
    PORTB = PORTB & B11011111;
    #else
    digitalWrite(LED_BUILTIN, HIGH);
    #endif
    String uwu = Serial.readString();
    Serial.println(sha1(String(uwu)));

    delay (1300);
    #if defined(ARDUINO_ARCH_AVR)
    PORTB = PORTB | B00100000;
    #else
    digitalWrite(LED_BUILTIN, LOW);
    #endif
} while (MM > 0);

}
