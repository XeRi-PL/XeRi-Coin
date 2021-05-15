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
delay(100);

}

void minersetup()

{
  //Serial.println("Block : " );
}

void loop(void) {

  // 24 H profit : 5,664384 BQU
  // 24 H profit =  $
  // 30 DAY's profit =  $

  Serial.println("Hello , Happy Mining !");
  miner();
}




void miner() {

  // usage as String
  // SHA1:a9993e364706816aba3e25717850c26c9cd0d89d

  //Serial.print("SHA1:");
  //Serial.println(sha1("abc"));

  // usage as ptr
  // SHA1:a94a8fe5ccb19ba61c4c0873d391e987982fbbd3

   delay (100);
  int a = 0;
  double MM = 0.00000001;
  int job = 0;
  double XRQC = 0.0037;
  do
  {
    
  uint8_t hash[10];
  sha1("test", &hash[0]);

  Serial.print("SHA1:");
  for (uint16_t i = 0; i < 10; i++) { Serial.print(hash[i]); }
      
    delay(450);
    Serial.println("Job : " + String(job) + "/" + String(job) + " * " + String(MM, DEC) +
    "XRQC " + " In session: " + String(XRQC * MM, DEC ) + " $" );
    delay (500);
    //Serial.println("Amount mined : " + String(XRQC * MM, DEC ) + " $ in XRQC" );

    minersetup();

    delay(25);
    PORTB = PORTB | B00100000;
    // Wait a bit
    delay(25);
    // Turn off built-in led
    PORTB = PORTB & B11011111;
    MM = MM + 0.00013112;
    job++;

  
  

  delay(1000);
} while (MM > 0);

}
