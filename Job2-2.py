from machine import Pin
import time

p1 = Pin(1,Pin.OUT)
p2 = Pin(2,Pin.OUT)
p3 = Pin(3,Pin.OUT)

while True:
    p1.on()
    time.sleep_ms(500)
    p1.off()
    time.sleep_ms(500)
    p2.on()
    time.sleep_ms(500)
    p2.off()
    time.sleep_ms(500)
    p3.on()
    time.sleep_ms(500)
    p3.off()
    time.sleep_ms(500)