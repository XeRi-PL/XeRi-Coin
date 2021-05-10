#include <stdio.h>
#include <math.h>


void setup()
{
  //otwarcie portu i ustawienie prędkości na 115200 bodów
  Serial.begin(115200);
  //while (!Serial);
  pinMode(LED_BUILTIN, OUTPUT);
  delay (5100);
}

// Xeri Coin Hasher
void minersetup()

{
  //Serial.println("Block : " );
}

// General Loop

void loop(void) {

  // 24 H profit : 5,664384 XRQ
  // 24 H profit =  $
  // 30 DAY's profit =  $

  Serial.println("Hello , Happy Mining !");
  miner();
}


void miner()
{
  delay (100);
  int a = 0;
  double MM = 0.00000001;
  int job = 0;
  double BQU = 0.0037;
  do
  {
    delay(450);
    Serial.println("XeRi-Coin * 2,00 s * 100H/s * Job Accepted : " + String(job) + "/" + String(job) + " * " + String(MM, DEC) + " Mined of XRQ" );
    delay (500);
    Serial.println("Amount mined : " + String(BQU * MM, DEC ) + " $ in BQU" );

    minersetup();

    delay(25);
    PORTB = PORTB | B00100000;
    // Wait a bit
    delay(25);
    // Turn off built-in led
    PORTB = PORTB & B11011111;
    MM = MM + 0.00013112;
    job++;

    delay (1000);

  } while (MM > 0);

}
