void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  char inputChar;
  inputChar = Serial.read();
  
  // put your main code here, to run repeatedly:
  if (inputChar == '1') {
    digitalWrite(LED_BUILTIN,HIGH);
  }
  if (inputChar == '0') {
      digitalWrite(LED_BUILTIN,LOW);
  }
}
