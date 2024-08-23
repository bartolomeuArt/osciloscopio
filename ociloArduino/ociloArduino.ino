// colocar referente a porta usada no arduino
int analogPin = A0;  

int val = 0; 

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1); 
}

void loop() {
  val = analogRead(analogPin);
  Serial.println(val);
}