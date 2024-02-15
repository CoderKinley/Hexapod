#include <SPI.h>
#include <RF24.h>

#define CE_PIN   9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN); // Create a Radio

const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address); // Set the address for writing data
}

void loop() {
  const char text[] = "Hello";
  radio.write(&text, sizeof(text)); // Send the message
  Serial.println("Message sent: Hello");
  delay(1000); // Wait for 1 second before sending again
}
