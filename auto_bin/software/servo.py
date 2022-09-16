from time import sleep
from machine import Pin, PWM
import umath

class Servo:

    def __init__(self, pin, freq=50, min_duty=40, max_duty=115, min_degs=0, max_degs=180):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.min_degs = min_degs
        self.max_degs = max_degs

    def set(self, degs):
        position = umath.interpolate(degs, self.min_degs, self.max_degs, self.min_duty, self.max_duty)
        self.pwm.duty(int(position))
