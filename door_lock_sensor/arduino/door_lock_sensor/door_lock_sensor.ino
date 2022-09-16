#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
 
// Set these to run example. 
#define FIREBASE_HOST "door-sensor-18524-default-rtdb.europe-west1.firebasedatabase.app" 
#define FIREBASE_AUTH "WTXR20mhI30UEXBZBHWRVCy9eQMOzRK2twCFV3gZ" 
#define WIFI_SSID "VM204198" 
#define WIFI_PASSWORD "es2fawYgzsRf" 
 
void setup() { 
  Serial.begin(9600); 
 
  // connect to wifi. 
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD); 
  Serial.print("connecting"); 
  while (WiFi.status() != WL_CONNECTED) { 
    Serial.print("."); 
    delay(500); 
  } 
  Serial.println(); 
  Serial.print("connected: "); 
  Serial.println(WiFi.localIP()); 
   
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH); 
} 
 
int n = 0; 
 
void loop() { 
  // set value 
  Firebase.setInt("number", n++); 
  // handle error 
  if (Firebase.failed()) { 
      Serial.print("setting /number failed:"); 
      Serial.println(Firebase.error());   
      return; 
  } 
  delay(1000);

}
