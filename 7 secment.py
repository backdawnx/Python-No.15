from machine import Pin
import time

# GPIO ports for the 7seg pins
segments = (0, 1, 2, 3, 4, 5, 6, 11)

# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
for segment in segments:
    Pin(segment, Pin.OUT)

# GPIO ports for the digit 0-3 pins
digits = (7, 8, 9, 10)

# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
for digit in digits:
    Pin(digit, Pin.OUT)

# (a, b, c, d, e, f, g, dp)
num = {' ': (0, 0, 0, 0, 0, 0, 0, 0),
       '0': (1, 1, 1, 1, 1, 1, 0, 0),
       '1': (0, 1, 1, 0, 0, 0, 0, 0),
       '2': (1, 1, 0, 1, 1, 0, 1, 0),
       '3': (1, 1, 1, 1, 0, 0, 1, 0),
       '4': (0, 1, 1, 0, 0, 1, 1, 0),
       '5': (1, 0, 1, 1, 0, 1, 1, 0),
       '6': (1, 0, 1, 1, 1, 1, 1, 0),
       '7': (1, 1, 1, 0, 0, 0, 0, 0),
       '8': (1, 1, 1, 1, 1, 1, 1, 0),
       '9': (1, 1, 1, 1, 0, 1, 1, 0),
       'b': (0, 0, 1, 1, 1, 1, 1, 0),  # Pattern for 'b'
       'y': (0, 1, 1, 1, 0, 1, 1, 0),
       'E': (1, 0, 0, 1, 1, 1, 1, 0),
       'A': (1, 1, 1, 0, 1, 1, 1, 0),
       'L': (0, 0, 0, 1, 1, 1, 0, 0),
       'X': (0, 1, 1, 0, 1, 1, 1, 0)}

def seg(display_string):
    for digit in range(4):
        for i, segment in enumerate(segments):
            Pin(segment, Pin.OUT).value(num[display_string[digit]][i])

        Pin(digits[digit], Pin.OUT).value(1)  # Turn on the digit

    time.sleep(0.5)  # Adjust this sleep time for the desired speed

    for digit in digits:
        Pin(digit, Pin.OUT).value(0)  # Turn off all digits

try:
    for n in range(10000):
        display_string = '{:04}'.format(n)
        seg(display_string)

finally:
    for segment in segments:
        Pin(segment, Pin.OUT).value(0)

    for digit in digits:
        Pin(digit, Pin.OUT).value(0)  # Turn off all digits
