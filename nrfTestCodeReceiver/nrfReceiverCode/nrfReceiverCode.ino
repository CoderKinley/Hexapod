#include <SPI.h>
#include <RF24.h>

#define CE_PIN   9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN); // Create a Radio

const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(1, address); // Set the address for reading data
  radio.startListening(); // Start listening for data
}

void loop() {
  if (radio.available()) {
    Serial.println("radio is avaliable");
    char text[32] = "";
    radio.read(&text, sizeof(text)); // Read the received message
    Serial.print("Received message: ");
    Serial.println(text);
  }
  else{
    Serial.println("Not Received anything!");
  }
}
