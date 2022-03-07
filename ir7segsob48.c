#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
int currentNumber = 0;
long codes[12]= //list of ir codes from remote
{0xFD30CF,0xFD08F7, //0,1
0xFD8877,0xFD48B7, //2,3
0xFD28D7,0xFDA857, //4,5
0xFD6897,0xFD18E7, //6,7
0xFD9867,0xFD56A7, //8,9
0xFD20DF,0xFD609F}; //advance, move back
int number[10][8] = // local storage for number outputs
{{0,0,0,1,0,0,0,1}, //0
{0,1,1,1,1,1,0,1}, //1
{0,0,1,0,0,0,1,1}, //2
{0,0,1,0,1,0,0,1}, //3
{0,1,0,0,1,1,0,1}, //4
{1,0,0,0,1,0,0,1}, //5
{1,0,0,0,0,0,0,1}, //6
{0,0,1,1,1,1,0,1}, //7
{0,0,0,0,0,0,0,1}, //8
{0,0,0,0,1,1,0,1}};//9
void numbershow(int i){ //number display
  for(int pin = 2; pin <= 9 ; pin++){
    digitalWrite(pin,number[i][pin - 2]);
  }
}
void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  for(int pin = 2; pin <=9; pin++){
    pinMode(pin,OUTPUT);
    digitalWrite(pin,HIGH);
  }
}
void loop(){
  if (irrecv.decode(&results)){
    for(int i = 0; i <= 11; i++){
      if(results.value == codes[i]&& i<=9){
        numbershow(i); //shows number on 7seg
        currentNumber = i;
        Serial.print(i);
        break;
      }
      else if(results.value == codes[10]&& currentNumber !=0){
        currentNumber--;
        numbershow(currentNumber);
        Serial.println(currentNumber);
        break;
      }
      else if(results.value == codes[10]&& currentNumber != 9){
        currentNumber++;numbershow(currentNumber);Serial.println(currentNumber);
        break;
      }
    }
    Serial.println(results.value, HEX);irrecv.resume();
  }
}