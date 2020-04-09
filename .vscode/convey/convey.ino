int motorPin = 3; //DC모터 핀 PWM제어
int LEDPin = 13;
int val;//가변저항 값, 속도 조절

void setup() {
  pinMode(motorPin,OUTPUT);//DC모터
  pinMode(LEDPin, OUTPUT);//LED,DC모터 작동 확인용
  Serial.begin(9600);
  while(! Serial)//시리얼 통신이 안 될 경우
  {
    digitalWrite(LEDPin,HIGH);//LED불 켜짐
    delay(100);
  }
  digitalWrite(LEDPin,LOW);//시리얼 통신되면 LED불 꺼짐
  delay(100);
  Serial.println("Ready");
  
}

void loop() {
  val = analogRead(A0);//가변저항 값

  int power = map(val,0,1023,0,1000);

  analogWrite(motorPin, power);//모터구동

  Serial.println(power);
}
