int incomingByte=0;
int pin=7;

void setup() {
  Serial.begin(9600); 
}

void loop() {
  // pour effectuer une action uniquement quand on recoit des données
  if(Serial.available()>0) {
    incomingByte=Serial.read();
    
    //aspiration
    if(incomingByte==1){
      digitalWrite(pin,HIGH); // on passe le pin à +5V 
    }
    
    //arret
    if(incomingByte==2){
      digitalWrite(pin,LOW)
    }
  }
}
