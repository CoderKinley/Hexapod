/* Code for NODE A */
#include <SPI.h>
#include "RF24.h"
RF24 radio(7,8); // for mega
byte node_A_address[6] = "NodeA";
byte node_B_address[6] = "NodeB";

void setup() {
  Serial.begin(115200);
  Serial.println(F("RF24/examples/GettingStarted"));

  radio.begin();

  radio.setPALevel(RF24_PA_LOW);

  radio.openWritingPipe(node_B_address);
  radio.openReadingPipe(1, node_A_address);
  radio.startListening();
}

void loop() {
  radio.stopListening();                                    

  Serial.println(F("Now sending Hello to node B"));

  char msg_to_B[20] = "Hello from node_A";                             
  
  unsigned long start_time = micros();      
  if (!radio.write( &msg_to_B, sizeof(msg_to_B) )) {
    Serial.println(F("failed to write message"));
  }

  radio.startListening();                                    // Now, continue listening

  unsigned long started_waiting_at = micros();               // Set up a timeout period, get the current microseconds
  boolean timeout = false;                                   // Set up a variable to indicate if a response was received or not
  while ( ! radio.available() ) {                            // While nothing is received
    if (micros() - started_waiting_at > 2000000 ) {           // If waited longer than 200ms, indicate timeout and exit while loop
      timeout = true;
      break;
    }
  }

  if ( timeout ) 
  {                                            // Describe the results
    Serial.println(F("Failed, response timed out."));
  } 
  else {
    char msg_from_B[20];                           
    radio.read( &msg_from_B, sizeof(msg_from_B) );
    unsigned long end_time = micros();
    Serial.print(F("Sent '"));
    Serial.print(msg_to_B);
    Serial.print(F("', Got response '"));
    Serial.print(msg_from_B);
    Serial.print(F("', Round-trip delay "));
    Serial.print(end_time - start_time);
    Serial.println(F(" microseconds"));
  }
  delay(2000);
}
