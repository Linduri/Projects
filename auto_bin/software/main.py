# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
print('Starting auto_bin...')

from time import sleep
from machine import Pin

print('Starting distance sensor...')
from hcsr04 import HCSR04
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

print('Starting servo...')
from servo import Servo
servo = Servo(5)
servo.set(0)

print('Starting dfmini...')
from dfplayer import SimpleDFPlayerMini
player = SimpleDFPlayerMini(1, 0, 1)

print('Playing wake noise...')
player.set_vol(30)
player.play()
#sleep(5)

print('Starting program loop...')


open_lid = False

while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')

    if distance < 10 and distance > 0:
        open_lid = True
        servo.set(0)
        print('Triggered at ', distance )
    else:
        servo.set(90)

    sleep(2)
    
