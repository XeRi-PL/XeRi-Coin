#include <Arduino.h>
#include "Hash.h"

#define LED_BUILTIN 2


void setup() {
Serial.begin(115200); // Start serial connection
delay(rand() % 1000); // delay up to 1sec to stagger start-ups
Serial.begin(115200);
delay(100);
pinMode(LED_BUILTIN, OUTPUT); // prepare for blink() function

}

void loop(void) {
  miner();

}

void minersetup()

{
  //Serial.println("Block : " );
}


void blink(uint8_t count, uint8_t pin = LED_BUILTIN) {
    uint8_t state = HIGH;

    for (int x=0; x<(count << 1); ++x) {
      digitalWrite(pin, state ^= HIGH);
      delay(50);
    }
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
    Serial.println(" - ESP Job : " + String(job) + "/" + String(job) + " * " + String(MM, DEC) +
    "XRQC " + " In session: " + String(XRQC * MM, DEC ) + " $" );
    delay (500);
    //Serial.println("Amount mined : " + String(XRQC * MM, DEC ) + " $ in XRQC" );

    //minersetup();

    MM = MM + 0.00013112;
    job++;

  
  

  delay(1000);
} while (MM > 0);

}
