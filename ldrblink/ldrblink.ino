void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(2,INPUT); //ldr pot divider
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lightval;
  lightval = analogRead(2);
  Serial.print(lightval);
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1024-lightval);                       // change wait time based on the ldr divider
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1024-lightval);                       // change wait time based on the ldr divider
}
