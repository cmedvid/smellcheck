int led = 2;
String readString;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("starting");
}

void loop() {
  while(!Serial.available()) 
  {
  } // wait cause words are correct
  
  while(Serial.available()>0) // words are wrong; activate the smellorama
  {
    char c = Serial.read();
    Serial.println(c);
    readString += c;
    Serial.println(readString);
    Serial.println("you got a word wrong, fool");
    for (int i = 0; i < 2; i++){
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW); 
      delay(500);
    }
    delay(2000);
    for (int i = 0; i < 3; i++){
      digitalWrite(led, HIGH);
      delay(500);
      digitalWrite(led, LOW); 
      delay(500);
    }
  }
}
