char incomingByte=0;
int pin=7;

void setup() {
  pinMode(pin,OUTPUT);
  Serial.begin(115200); 
}

void loop() {
  // pour effectuer une action uniquement quand on recoit des données
  if(Serial.available()>0) {
    incomingByte=Serial.read();
    Serial.println(incomingByte); // write a string
    delay(1000);
    //aspiration
    if(incomingByte==49){
      digitalWrite(pin,HIGH); // on passe le pin à +5V 
    }
    
    //arret
    if(incomingByte=='2'){
      digitalWrite(pin,LOW);
    }
  }
}
