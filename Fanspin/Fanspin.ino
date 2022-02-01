void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT); //Pin for the fan relay
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13, HIGH);   //sets fan to spin
  delay(3000);              //lets fan spin for 3 secconds        
  digitalWrite(13, LOW);    //stops fan from spinning
  delay(5000);
}
