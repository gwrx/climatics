#!/bin/python3

import RPi.GPIO as GPIO
from time import sleep

class coins():

    # value:channel
    value2channel = {2:2, 1:3, 0.5:4}
    # channel:value
    channel2value = {2:2, 3:1, 4:0.5}

    credit = 0

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(value2channel[0.5], GPIO.IN)
        GPIO.setup(value2channel[1], GPIO.IN)
        GPIO.setup(value2channel[2], GPIO.IN)

        GPIO.add_event_detect(value2channel[0.5],
                              GPIO.FALLING, callback=coinInserted)
        GPIO.add_event_detect(value2channel[1],
                              GPIO.FALLING, callback=coinInserted)
        GPIO.add_event_detect(value2channel[2],
                              GPIO.FALLING, callback=coinInserted)

    def coinInserted(channel):
        self.credit += channel2value[channel]
        print("Euro: " + channel2value[channel])

    def getCredit(self):
        return self.credit

    def __del__(self):
        GPIO.cleanup()

