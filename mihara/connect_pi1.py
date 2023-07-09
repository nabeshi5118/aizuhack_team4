#mihara
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

IN = 14
OUT = 15


GPIO.setup(IN, GPIO.IN)
GPIO.setup(OUT, GPIO.OUT, initial = GPIO.LOW)

GPIO.output(OUT, GPIO.HIGH)


GPIO.cleanup()



#if GPIO.input(IN) == GPIO.HIGH:
    #print("IN")
#else:
    #print("OUT")