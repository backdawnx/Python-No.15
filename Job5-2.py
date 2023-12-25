from machine import ADC, Pin
import time

# Define the ADC pin
adc_pin = Pin(26, Pin.IN)

# Create ADC object
adc = ADC(26)

while True:
    analog_value = adc.read()
    print("Analog Value:", analog_value)
    time.sleep(0.2)
