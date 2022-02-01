void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("11 int on, 10 int off, 21 ext on, 20 ext off");
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int option;
  while(Serial.available()){
    option = Serial.readString().toInt();
      Serial.print(option);
      switch (option){
        case 11:
          digitalWrite(13,HIGH);
          Serial.println("on");
          break;
        case 10:
          digitalWrite(13,LOW);
          Serial.println("off");
          break;
        case 21:
          digitalWrite(12,HIGH);
          Serial.println("on");
          break;
        case 20:
          digitalWrite(12,LOW);
          Serial.println("off");
          break;
      }
  }
}
