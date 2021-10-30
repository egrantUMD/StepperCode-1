import time
import json
from stepperA import stepper
from stepperA import PCF8591
import RPi.GPIO as GPIO
from time import sleep
import smbus


step = stepper()
GPIO.setmode(GPIO.BCM)

light = 4
pins = [18,21,22,23]
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

GPIO.setup(light, GPIO.OUT, initial=0)

angle2 = 0
brightness = 0
while True:
  with open('/lib/cgi-bin/angle.txt', 'r') as f:
    data = json.load(f)
    p1 = str(data['mode'])
    slide = int(data['slider1'])
  angle = slide
  if angle > angle2 and p1 == 'Submit Angle':
    a = angle - angle2
    b = 360 - a
    if a>=b:
      step.goangle(b, -1 )
    elif a < b:
      step.goangle(a, 1)
    angle2 = angle
  elif angle < angle2 and p1 == 'Submit Angle':
    a = angle2 - angle
    b = 360 - a
    if a>=b:
      step.goangle(b, 1 )
    elif a < b:
      step.goangle(a, -1)
    angle2 = angle
  elif p1 == 'Zero Motor':
    GPIO.output(light, 1)
    while brightness < 190:
      brightness = step.zero()
    GPIO.output(light, 0)

  





