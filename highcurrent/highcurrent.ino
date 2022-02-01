void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(0,INPUT_PULLUP);
  attachInterrupt(0,highrupt,RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i < 9; i++){
    //Serial.print(i);
    }
}

void highrupt(){
  Serial.print("HIGH");
  digitalWrite(13,HIGH);
}
