 // Read in a character from serial.  If it's '1', turn the built-in LED on.  If it's '0', turn it off.
  
void setup() {
  // Start the serial port
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  char inputChar;
  inputChar = Serial.read(); // Read in a character
  
  if (inputChar == '1') {    // If it's a '1', turn on the LED
    digitalWrite(LED_BUILTIN,HIGH);
  }
  if (inputChar == '0') {    // If it's a '0', turn off the LED
      digitalWrite(LED_BUILTIN,LOW);
  }
}
