# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
print('Starting auto_bin...')

from hcsr04 import HCSR04
from time import sleep

print('Starting distance sensor...')
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

print('Starting program loop...')
while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')

    if distance < 30 and distance > 0:
        print('Triggered at ', distance )

    sleep(1)