# coding: utf-8
import sys
import time
import RPi.GPIO as GPIO

BEEPER_PIN = 4
co2 = int(sys.argv[1])
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BEEPER_PIN, GPIO.OUT)


def beep():
    beeper_count = 0 if co2 < 700 else 2 if co2 < 1000 else 3 if co2 < 1500 else 4
    for _ in range(beeper_count):
        GPIO.output(BEEPER_PIN, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(BEEPER_PIN, GPIO.LOW)
        time.sleep(0.2)


if __name__ == "__main__":
    beep()
