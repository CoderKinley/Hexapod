/* Code for NODE B */

#include <SPI.h>
#include "RF24.h"

RF24 radio(7,8); // this is for arduino mega
byte node_A_address[6] = "NodeA";
byte node_B_address[6] = "NodeB";

void setup() {
  Serial.begin(115200);
  Serial.println(F("RF24/examples/GettingStarted"));

  radio.begin();
  radio.setPALevel(RF24_PA_LOW);
  radio.openWritingPipe(node_A_address);
  radio.openReadingPipe(1, node_B_address);
  radio.startListening();
}

void loop() {
  char msg_from_A[20];

  if ( radio.available()) {
    while (radio.available()) {                                  
      radio.read( &msg_from_A, sizeof(msg_from_A) );
    }
    radio.stopListening();                             

    char msg_to_A[20] = "Hello from node_B";
    radio.write( &msg_to_A, sizeof(msg_to_A) );             
    radio.startListening();                                     
    
    Serial.print(F("Got message '"));0
    Serial.print(msg_from_A);
    Serial.print(F("', Sent response '"));
    Serial.print(msg_to_A);
    Serial.println(F("'"));
  }

}
