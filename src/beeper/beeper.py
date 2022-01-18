import sys
import time
import RPi.GPIO as GPIO

co2 = sys.argv()[1]
BEEPER_PIN = 4
GPIO.setmode(GPIO.BSM)
GPIO.setup(4, BEEPER_PIN)


def beep():
    beeper_count = 0 if co2 < 700 else 1 if co2 < 1000 else 2 if co2 < 1500 else 3
    for _ in beeper_count:
        GPIO.output(BEEPER_PIN, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(BEEPER_PIN, GPIO.LOW)
        time.sleep(0.2)


if __name__ == "__main__":
    beep()
