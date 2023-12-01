const int pinX = A0; // Conectado al eje X en el pin analógico A0
const int pinY = A1; // Conectado al eje Y en el pin analógico A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Ejemplo de lectura de valores analógicos del joystick
  int xValue = analogRead(pinX);
  int yValue = analogRead(pinY);

  // Envío de datos a través del puerto serial a la PC
  Serial.print("X:");
  Serial.print(xValue);
  Serial.print(",Y:");
  Serial.println(yValue);

  delay(100); // Espera para evitar envío continuo
}
