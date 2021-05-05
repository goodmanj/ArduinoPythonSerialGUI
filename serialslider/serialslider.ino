byte inputByte = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    inputByte = Serial.read();
    digitalWrite(LED_BUILTIN,HIGH);
    delay(inputByte*10);
    digitalWrite(LED_BUILTIN,LOW);
  }
}
