# IoT26-HW02_SeolJaemin.py
# 202234900 Seol Jaemin

from gpiozero import Button, LED # or DigitalInputDevice, DigitalOutputDevice
from signal import pause

led = LED(14) # LED is on GPIO14 = pin8
button = Button(4) # Button is on GPIO4 = pin7

# On when pressed
# button.when_pressed = led.on
# button.when_released = led.off

# toggle when pressed
button.when_pressed = led.toggle

pause()