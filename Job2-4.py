from machine import Pin, ADC, PWM         
                           

led = PWM(Pin(1))           
led.freq(1000)

potentiometer = ADC(28)         

while True:
  value = potentiometer.read_u16()        
  print(value)
  led.duty_u16(value)           
