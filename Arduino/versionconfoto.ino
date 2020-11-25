#include "DHT.h" 
const unsigned int PIN_LED = 10;
const unsigned int PIN_LED2 = 11;
const unsigned int PIN_LED3 = 13;
const unsigned int PIN_LED4 = 12;
const long PERIODO = 1000;
const unsigned int BAUD_RATE = 9600;
int estadoLed = LOW;
int estadoLed2= LOW;
int estadoLed3= LOW;
int estadoLed4= LOW;
int controlPir=LOW;
unsigned long lapsoAnterior = 0;
const int PIN_PIR = 2;
const int PIN_BUZZER = 9;
int estadoAntLed = LOW; // Etado anterior del PIR
int estadoAntLed2 = LOW;
int estadoAntLed3= LOW;
int estadoAntLed4 =LOW;
int estadoAntPir=LOW;
const unsigned int PIN_DHT = 3; 
DHT dht(PIN_DHT, DHT11); 
int val;
const unsigned int PIN_FLAMA = 4;
const unsigned int CONTROL_PIR=5;
char comando;
const int PIN_FOTORES = A1;
const int PIN_FOTORES2=A2;


void setup() {
 pinMode(PIN_LED, OUTPUT);
 pinMode(PIN_LED2, OUTPUT);
 pinMode(PIN_LED3, OUTPUT);
 pinMode(PIN_LED4, OUTPUT);
 pinMode(PIN_PIR, INPUT);
 pinMode(PIN_BUZZER, OUTPUT);
 pinMode(PIN_FLAMA, INPUT);
 Serial.begin(BAUD_RATE);
 dht.begin();
}

 //-----CONTROL FOTORES
float leer() {
  int nivelLuz = analogRead(PIN_FOTORES);
  float valor = nivelLuz * (5.0 / 1023.0);

  return valor;
 }
 
void secuencia1(){
  digitalWrite(PIN_LED, HIGH);
  delay(500);
  digitalWrite(PIN_LED, LOW);
  delay(250);
  digitalWrite(PIN_LED3, HIGH);
  delay(500);
  digitalWrite(PIN_LED2, HIGH);
  delay(500);
  digitalWrite(PIN_LED2, LOW);
}


 //------------------------

void loop() {

 //-----------CONTROL FOTORES-------
 int nivelLuz = analogRead(PIN_FOTORES);
 float valor = nivelLuz * (5.0 / 1023.0);
 float valorn = valor;


 //-----------------------------------

 

 //----------CONTROL LEDS--------------------
if(Serial.available()){
    comando = Serial.read();
    if(comando == 'Z'){
      estadoLed = HIGH;
      digitalWrite(PIN_LED2, estadoLed);
      delay(50);
    }
    if(comando == 'Y'){
      estadoLed = LOW;
      digitalWrite(PIN_LED2, estadoLed);
      delay(50);
    }
    if(comando == 'X'){
      estadoLed2 = HIGH;
      digitalWrite(PIN_LED3, estadoLed2);
      delay(50);
    }
    if(comando == 'W'){
      estadoLed2 = LOW;
      digitalWrite(PIN_LED3, estadoLed2);
      delay(50);
    }
    if(comando == 'V'){
      estadoLed3 = HIGH;
      digitalWrite(PIN_LED4, estadoLed3);
      delay(50);
    }
    if(comando == 'U'){
      estadoLed3 = LOW;
      digitalWrite(PIN_LED4, estadoLed3);
      delay(50);
    }
    if(comando == 'T'){
      estadoLed4 = HIGH;
      digitalWrite(PIN_LED, estadoLed4);
      delay(50);
    }
    if(comando == 'S'){
      estadoLed4 = LOW;
      digitalWrite(PIN_LED, estadoLed4); 
      delay(50);     
    }
    if(comando == 'A'){
      controlPir = HIGH;
      digitalWrite(CONTROL_PIR, controlPir);
      delay(50);
    }
    if(comando == 'B'){
      controlPir = LOW;
      digitalWrite(CONTROL_PIR, controlPir);
      delay(50);
    }
    if(comando == 'C'){
      secuencia1();
      Serial.println("Secuencia1");
      delay(50);
    }
  
    
 }

 if(estadoLed == HIGH){
  if(estadoAntLed == LOW){
    valorn=leer();
    if(valorn>=2){
    Serial.println("LED1ON");
   estadoAntLed = HIGH;
    }else{
     Serial.println("noprendio");
    }
    
 
  }
   
 }else if(estadoLed == LOW){
  if(estadoAntLed == HIGH){
    valorn=leer();
    if(valorn<2){
    Serial.println("LED1OFF");
   estadoAntLed = LOW;
    }else{
     Serial.println("noapago");
    }
  }
 }

 if(estadoLed2 == HIGH){
  if(estadoAntLed2 == LOW){
    
      Serial.println("LED2ON");
       estadoAntLed2 = HIGH; 
    }
     
  }
   
 else if(estadoLed2 == LOW){
  if(estadoAntLed2 == HIGH){
    
      Serial.println("LED2OFF");
      estadoAntLed2= LOW;
   
  }
 }

if(estadoLed3 == HIGH){
  if(estadoAntLed3 == LOW){
   
         Serial.println("LED3ON");
         estadoAntLed3 = HIGH;
    
  }
   
 }else if(estadoLed3 == LOW){
  if(estadoAntLed3 == HIGH){    
         Serial.println("LED3OFF");
         estadoAntLed3 = LOW;
  }
 }

 if(estadoLed4 == HIGH){
  if(estadoAntLed4 == LOW){
   Serial.println("LED4ON");
   estadoAntLed4 = HIGH;
  }
   
 }else if(estadoLed4 == LOW){
  if(estadoAntLed4 == HIGH){
    Serial.println("LED4OFF");
    estadoAntLed4= LOW;
  }
 }
 
 
//--------------------------------------------



//------CONTROL PIR/BUZZER---------------------
  
   if(controlPir == HIGH){
    int valorPir = digitalRead(PIN_PIR);
    // Si se detecta movimiento
    if (valorPir == HIGH) {
      // Si no habia movimiento anteriormente
      if (estadoAntPir == LOW) {
        Serial.println("PIRON");
        tone(PIN_BUZZER, 500);
        delay(500);
        noTone(PIN_BUZZER);
        delay(500);  
        // Hay movimiento
        estadoAntPir = HIGH;
      }
    }
    // Si no se detecto movimiento
    else {
      // Si habia movimiento anteriormente
      if (estadoAntPir == HIGH) {
        Serial.println("PIROFF");
        // No hay movimiento
        estadoAntPir = LOW;
      }
    }
  }
//--------------------------------------


//-------------CONTROL DHT----------------
// Espere unos segundos entre lecturas. La lectura de la
 // temperatura y humedadtoma unos 250 ms. Depende del sensor
 //delay(1000);

 // Lee la humedad
 float h = dht.readHumidity();

 // Lee la temperatura en grados Celsius (por omision)
 float tc = dht.readTemperature();

 // Lee la temperatura en grados Fahrenheit
 //(isFahrenheit = true)
 float tf = dht.readTemperature(true);

 // Verifica si alguna lectura fallo y aborta
 // (para intentar de nuevo).
 if (isnan(h) || isnan(tc) || isnan(tf)) {
 Serial.println("Fallo la lectura del sensor DHT!");
 return;
 }

 // Calcula el indice de calor en grados Fahrenheit
 // (por omision)
 float hif = dht.computeHeatIndex(tf, h);
 // Calcula el indice de calor en grados Celsius
 // (isFahreheit = false)
 float hic = dht.computeHeatIndex(tc, h, false);

/*
 Serial.print("Humedad:"  );
 Serial.println(h);
 Serial.print("Temperatura: ");
 Serial.print(tc);
 Serial.print(" *C ");
 Serial.println(tf);
 Serial.print("Indice de calor: ");
 Serial.print(hic);
 Serial.print(" *C ");
 Serial.print(hif); 
 Serial.println(" *F"); 
*/


 Serial.print(":");
 Serial.print(h);
 Serial.print(":");
 Serial.print(tc);
 Serial.print(" *C");
 Serial.print(tf);
 Serial.print(":");
 Serial.print(hic);
 Serial.print(" *C ");
 Serial.print(hif);
 Serial.print(" *F");
 Serial.println(":");


//-------------------------------------------
 

//------------------CONTROL FLAMA-------------
val = digitalRead(PIN_FLAMA);
  if(val == HIGH){
    tone(PIN_BUZZER,1000,1000);
    Serial.println("fon");
    val= LOW;
    //delay(2000);
  }else{
    noTone(PIN_BUZZER);
  }
//---------------------------------------------
delay(250);
}
