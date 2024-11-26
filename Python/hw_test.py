from gpiozero import LED, Buzzer
from time import sleep

led = LED(23)
buzzer = Buzzer(18)

try:
    while True:
        led.on()
        buzzer.on()
        sleep(1)
        
        led.off()
        buzzer.off()
        sleep(1)
        
except KeyboardInterrupt:
    led.off()
    buzzer.off()
    
    