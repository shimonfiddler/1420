void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(2,INPUT);
  attachInterrupt(0,highprint,RISING);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0;i<10;i++){
    Serial.print(i);
    }
}

void highprint(){
  Serial.print("HIGH");
  //digitalWrite(13,HIGH);
  
}
