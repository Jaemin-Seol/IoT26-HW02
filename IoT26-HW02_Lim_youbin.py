#Lim_youbin
from gpiozero import Button, LED
from time import sleep

led = LED(14)
button = Button(4)

while True:
    if button.is_pressed:
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)

        led.on()
        sleep(0.1)
        led.off()
        sleep(0.3) 

    else:
        led.off()
        sleep(0.1)
