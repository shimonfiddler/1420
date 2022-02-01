int motor = 5;
int speed = 0;
int fadeAmount = 1;

void setup(){
  pinMode(motor, OUTPUT);
  pinMode(2,INPUT_PULLUP);
  Serial.begin(9600);
  attachInterrupt(0, HI, CHANGE);
  //attachInterrupt(0, LO, FALLING);
}

void loop() {
  //analogWrite(motor, speed);
  //speed = speed + fadeAmount;
  
  //if (speed <= 0 || speed >= 250){
    //fadeAmount = -fadeAmount;
  //}
  
  //delay(10);
  //if(digitalRead(2) == HIGH){
  //	digitalWrite(motor,HIGH);
  //}
  if(analogRead(A0>=200)){
    analogWrite(motor,255);
  }
}

void HI(){
  Serial.println("1");
}