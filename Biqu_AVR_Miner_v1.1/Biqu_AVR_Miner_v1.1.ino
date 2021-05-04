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

// BiquCoin Hasher
void minersetup(void)

{
  //Serial.println("Block : " );
}

// General Loop

void loop(void) {

  // 24 H profit : 5,664384 BQU
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
    Serial.println("Biqu-Coin * 2,00 s * 100H/s * Job Accepted : " + String(job) + "/" + String(job) + " * " + String(MM, DEC) + " Mined of BQU" );
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
