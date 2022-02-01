void setup() {
  // put your setup code here, to run once:
  pinMode(11,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int pwmrate;
  pwmrate = 0;
  while(pwmrate < 255){ 
    analogWrite(11,pwmrate);
    delay(10);
    pwmrate = pwmrate + 1;
  }
 while(pwmrate > 0){ 
    analogWrite(11,pwmrate);
    delay(10);
    pwmrate = pwmrate - 1;
  }
}
