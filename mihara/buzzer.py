#mihara
import time
import datetime
import RPi.GPIO as GPIO
import sys

def alarm_ON():
    pwm.start(100)
    time.sleep(5)

def alarm_OFF():
    pwm.stop()


GPIO.setmode(GPIO.BCM)

BUZZER = 18
BUTTON = 5
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(BUZZER,100)
     
dt_now = datetime.datetime.now()
# 無限ループ
H = 18
M = 59
print(dt_now)
now_H = dt_now.hour
now_M = dt_now.minute




while(True):
    #アラームの時刻を後で入れる
    if now_H == 19 and now_M == 26:
        alarm_ON()
        break
while(True):
    if GPIO.input(BUTTON) == GPIO.HIGH:
        alarm_OFF()
        print("OFF")
        break
         
# GPIOの設定をリセット
GPIO.cleanup()