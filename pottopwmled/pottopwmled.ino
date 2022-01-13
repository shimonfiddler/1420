int x; //pot value
int y; //for processing value
int outpin;//for assigning the output pin

  
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //starts the serial connection
  pinMode(A3,INPUT); //Input from pot
  pinMode(3,OUTPUT); //pwm output
  pinMode(5,OUTPUT); //2nd pwm output
  pinMode(4,INPUT); //Input button press
  outpin = 3;
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(4==HIGH)){ //swaps led output each button press
    if (outpin == 3){
      outpin = 5;
    }
    else{
      outpin = 3;
    }
  }
  x = analogRead(A3); //reads pot
  Serial.println(x); //pot raw value to serial terminal(for debugging)
  y = map(x,0,1023,0,254); //maps the input od adc to a value dac can use properly
  analogWrite(outpin,x); //writes the vale as apwm signal
}
