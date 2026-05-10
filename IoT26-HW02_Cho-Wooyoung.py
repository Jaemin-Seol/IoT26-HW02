# gpiozero: controls raspberrypi pins
from gpiozero import Button, LED
from signal import pause

# led assign gpio pin 14
led = LED(14)
# button assign gpio pin 4
button = Button(4)

# led on while pressed, off when released
button.when_pressed = led.on
button.when_released = led.off

# keeps the process alive while waiting for button event
pause()
