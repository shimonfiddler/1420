void setup() {
  // put your setup code here, to run once:
  pinMode(11,OUTPUT); //output to buzzer
}

void loop() {
  // put your main code here, to run repeatedly:
  int pwmrate;
  pwmrate = 0; //sets the pwm to minimum
  while(pwmrate < 255){ //loop for increasing the pwm signal gradualy
    analogWrite(11,pwmrate);
    delay(10); //delay for each increase in pwm signal
    pwmrate = pwmrate + 1;
  }
 while(pwmrate > 0){ //loop for decreasing the pwm signal
    analogWrite(11,pwmrate);
    delay(10);
    pwmrate = pwmrate - 1;
  }
}
