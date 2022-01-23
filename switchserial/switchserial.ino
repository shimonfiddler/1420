void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int option;
  while(Serial.available()){
    option = Serial.readString();
    Serial.print(option);
    switch (option){
      case 'on':
        digitalWrite(13,HIGH);
        break;
      case 'off':
        digitalWrite(13,LOW);
        break;
    }
  }
  

}
