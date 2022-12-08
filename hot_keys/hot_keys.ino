#include <Wire.h> 

void setup()
{
  Serial.begin(9600);  
  while (!Serial) {  ;  }
  digitalWrite(8, LOW);
  pinMode(8, INPUT); 
  pinMode(8, INPUT);
  digitalWrite(9, LOW);    
}


void loop()
{
  //Serial.println(digitalRead(8));
  if (floor(digitalRead(8)) == HIGH){
  Serial.println("1");
  digitalWrite(8, LOW); 
  delay(3000);
 // Serial.println("0");
  }

  if (floor(digitalRead(9)) == HIGH){
  Serial.println("2");
  while (digitalRead(9) == HIGH){
    //Serial.println("looping..");
    ;}
  delay(3000);
 // Serial.println("0");
  }

  if (floor(digitalRead(10)) == HIGH){
  Serial.println("3");
  while (digitalRead(10) == HIGH){
    //Serial.println("looping..");
    ;}
  delay(3000);
 // Serial.println("0");
  }
}
