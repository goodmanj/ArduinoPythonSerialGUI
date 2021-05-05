 // Read in a byte from serial.  Blink the LED for a duration that depends on the byte read.
 
byte inputByte = 0;

void setup() {
  // Start the serial port
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {  // If there's serial data to read
    inputByte = Serial.read();   // Read in one byte (char)
    digitalWrite(LED_BUILTIN,HIGH);  
    delay(inputByte*10);         // Delay for 10 times that many milliseconds.
    digitalWrite(LED_BUILTIN,LOW);
  }
}
