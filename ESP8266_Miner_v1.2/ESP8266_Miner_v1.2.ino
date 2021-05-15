#include <ESP8266WiFi.h> // Include WiFi library
#include <ESP8266mDNS.h> // OTA libraries
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include "Hash.h"

namespace {
const char* ssid          = "SSID";   // Change this to your WiFi SSID
const char* password      = "PASSWORD WIFI";    // Change this to your WiFi password
const char* ducouser      = "USER";     // Change this to your XeRi-Coin username
const char* rigIdentifier = "USER PASSWORD";       // Change this if you want a custom miner name

const char * host = "127.0.0.1"; // Static server IP
const int port = 1233;
unsigned int Shares = 0; // Share variable

  WiFiClient client;
  String clientBuffer = "";

  #define END_TOKEN  '\n'
  #define SEP_TOKEN  ','

  #define LED_BUILTIN 2

  #define BLINK_SHARE_FOUND    1
  #define BLINK_SETUP_COMPLETE 2
  #define BLINK_CLIENT_CONNECT 3
  #define BLINK_RESET_DEVICE   5

  void SetupWifi() {
    Serial.println("Connecting to: " + String(ssid));
    WiFi.mode(WIFI_STA); // Setup ESP in client mode
    WiFi.begin(ssid, password); // Connect to wifi

    int wait_passes = 0;
    while (WiFi.waitForConnectResult() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
      if (++wait_passes >= 10) {
        WiFi.begin(ssid, password);
        wait_passes = 0;
      }
    }

    Serial.println("\nConnected to WiFi!");
    Serial.println("Local IP address: " + WiFi.localIP().toString());
  }

  void SetupOTA() {
    ArduinoOTA.onStart([]() { // Prepare OTA stuff
      Serial.println("Start");
    });
    ArduinoOTA.onEnd([]() {
      Serial.println("\nEnd");
    });
    ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
      Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
    });
    ArduinoOTA.onError([](ota_error_t error) {
      Serial.printf("Error[%u]: ", error);
      if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
      else if (error == OTA_BEGIN_ERROR) Serial.println("Begin Failed");
      else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
      else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
      else if (error == OTA_END_ERROR) Serial.println("End Failed");
    });

    ArduinoOTA.setHostname(rigIdentifier); // Give port a name not just address
    ArduinoOTA.begin();
  }

  void blink(uint8_t count, uint8_t pin = LED_BUILTIN) {
    uint8_t state = HIGH;

    for (int x=0; x<(count << 1); ++x) {
      digitalWrite(pin, state ^= HIGH);
      delay(50);
    }
  }

  void RestartESP(String msg) {
    Serial.println(msg);
    Serial.println("Resetting ESP...");
    blink(BLINK_RESET_DEVICE); 
    ESP.reset();
  }

  void handleSystemEvents(void) {
    ArduinoOTA.handle();
    yield();
  }

  String getValue(String data, char separator, int index)
  {
    int found = 0;
    int strIndex[] = {0, -1};
    int maxIndex = data.length()-1;

    for(int i=0; i<=maxIndex && found<=index; i++){
      if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
      }
    }

    return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
  }
  
  void waitForClientData(void) {
    clientBuffer = "";
    
    while (client.connected()) {
      if (client.available()) {
        clientBuffer = client.readStringUntil(END_TOKEN);
        if (clientBuffer.length() == 1 && clientBuffer[0] == END_TOKEN)
          clientBuffer = "???\n"; // NOTE: Should never happen...

        break;
      }
      handleSystemEvents();
    }
  }

  void ConnectToServer() {
    if (client.connected())
      return;

    Serial.println("\nConnecting to XRQC server...");
 
    Serial.println("Connected to the server. Server Beta version: v1.2");
    blink(BLINK_CLIENT_CONNECT); // Blink 3 times - indicate sucessfull connection with the server
  }

  bool max_micros_elapsed(unsigned long current, unsigned long max_elapsed) {
    static unsigned long _start = 0;

    if ((current - _start) > max_elapsed) {
      _start = current;
      return true;
    }
      
    return false;
  }
} // namespace

void setup() {
  Serial.begin(115200); // Start serial connection
  Serial.println("\nXeRi-Coin ESP8266 Miner Beta v1.2");

  delay(rand() % 1000); // delay up to 1sec to stagger start-ups
  pinMode(LED_BUILTIN, OUTPUT); // prepare for blink() function

  SetupWifi();
  SetupOTA();

  blink(BLINK_SETUP_COMPLETE); // Blink 2 times - indicate sucessfull connection with wifi network
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
