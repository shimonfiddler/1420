int n1 = 2;
int n2 = 3;
int n3 = 4;
int n4 = 5;
int n5 = 6;
int n6 = 7;
int n7 = 8;
int n8 = 9;
int s = 10;
void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
int potval = analogRead(A0);
if (potval < 128 and potval > 0) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, LOW);
  digitalWrite(n3, LOW);
  digitalWrite(n4, LOW);
  digitalWrite(n5, LOW);
  digitalWrite(n6, LOW);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 256 and potval > 129) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, LOW);
  digitalWrite(n4, LOW);
  digitalWrite(n5, LOW);
  digitalWrite(n6, LOW);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 384 and potval > 257) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, LOW);
  digitalWrite(n5, LOW);
  digitalWrite(n6, LOW);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 512 and potval > 385) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, HIGH);
  digitalWrite(n5, LOW);
  digitalWrite(n6, LOW);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 640 and potval > 513) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, HIGH);
  digitalWrite(n5, HIGH);
  digitalWrite(n6, LOW);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 768 and potval > 641) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, HIGH);
  digitalWrite(n5, HIGH);
  digitalWrite(n6, HIGH);
  digitalWrite(n7, LOW);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 896 and potval > 769) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, HIGH);
  digitalWrite(n5, HIGH);
  digitalWrite(n6, HIGH);
  digitalWrite(n7, HIGH);
  digitalWrite(n8, LOW);
  digitalWrite(s, HIGH);
  }
if (potval < 1023 and potval > 897) {
  digitalWrite(n1, HIGH);
  digitalWrite(n2, HIGH);
  digitalWrite(n3, HIGH);
  digitalWrite(n4, HIGH);
  digitalWrite(n5, HIGH);
  digitalWrite(n6, HIGH);
  digitalWrite(n7, HIGH);
  digitalWrite(n8, HIGH);
  digitalWrite(s, HIGH);
  }
Serial.println(potval);
delay(100);
}
