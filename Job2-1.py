from machine import Pin
import time

p1 = Pin(1,Pin.OUT)


while (1):
    p1.on()
    time.sleep_ms(500)
    p1.off()
    time.sleep_ms(500)