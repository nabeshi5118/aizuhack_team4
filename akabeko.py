#モジュールのインポート

#課題取得のモジュール
import

#音声認識のモジュール
import

#アラームの時刻設定のモジュール
import

#ブザーのモジュール
import time
import datetime
import RPi.GPIO as GPIO
import sys


#関数

#ブザーを鳴らす関数
def alarm_ON():
    pwm.start(100)
    time.sleep(5)

def alarm_OFF():
    pwm.stop()


#ピン設定

#ブザー
GPIO.setmode(GPIO.BCM)

BUZZER = 18
BUTTON = 5

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)



#処理
#ブザーを鳴らす
while(True):
    if now_H == alarm_hour and now_M == alarm_min:
        alarm_ON()
        break
while(True):
    if GPIO.input(BUTTON) == GPIO.HIGH:
        alarm_OFF()
        print("OFF")
        break

#GPIOのピンをリセット
GPIO.cleanup()