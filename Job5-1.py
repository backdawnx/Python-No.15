from machine import Pin
from time import sleep

led = Pin(27, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)  
