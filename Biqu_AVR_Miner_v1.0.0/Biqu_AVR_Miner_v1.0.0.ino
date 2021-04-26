#include<stdio.h>
#include <math.h>


void setup() {
  //otwarcie portu i ustawienie prędkości na 9600 bodów
  Serial.begin(115200);
  randomSeed(analogRead(0));
  while (!Serial);
  Serial.println("Witaj milego koapnia!");
  delay (5100);
}


void loop() {

  delay (10);
  int a = 0;
  double MM = 0.0000000001;
  int job = 0;



  
  do
  {
    Serial.println("Block Hash: " + random(10000000000));
    Serial.println("Biqu-Coin * 1,35s * 100H/s * Job Accepted : " + String(job) + "/" + String(job) + " * " + String(MM, DEC) + " Mined of BQU" );

    delay (300);
    MM = MM + 0.0000006556;
    job++;
    delay (1000);

  } while (a == 0);

  return;
}
