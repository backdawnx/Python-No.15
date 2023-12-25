from machine import Pin, I2C
from time import sleep
import dht
from ssd1306 import SSD1306_I2C


# Initialize the I2C OLED display
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Initialize the DHT22 sensor
sensor = dht.DHT22(Pin(0))

while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    # Format the temperature and humidity data
    display_text = "Temp: {}°C\nHumidity: {}%".format(temp, hum)

    # Clear the OLED display
    oled.fill(0)

    # Display the data on the OLED display
    oled.text(display_text, 0, 0)

    # Update the OLED display
    oled.show()

    sleep(2)
