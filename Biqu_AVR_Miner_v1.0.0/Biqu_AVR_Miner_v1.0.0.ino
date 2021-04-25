#include<stdio.h>
#include <math.h>
#include "hash.c"

void setup() {
  //otwarcie portu i ustawienie prędkości na 9600 bodów
  Serial.begin(115200);
  while(!Serial);
  Serial.println("Witaj milego koapnia!");
  delay (5100);
}
 
int a = 0;
 
void loop(void) {

  delay (300);
  int a = 0;
  double MM = 0.0000000001;
  int job = 0;
  do
  {
    Serial.println("Biqu-Coin * 1,35s * 100H/s * Job Accepted : " + String(job) + " * "+ String(MM,DEC) + " Mined of BQU" );
    
    delay (300);
    MM = MM + 0.0000006556;
    job++;
    delay (1000);
  } while (a == 0);
  return;
}
