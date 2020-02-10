from machine import Pin
import time
import utime

import random

import utils

config = utils.load_config()

def doCleaning():
    weekday = utime.localtime()[6]
    if weekday not in config["behavior"]["weekdays"]:
        print("doCleaning: Not today :-(")
        return False

    hour = utime.localtime()[3]
    if hour not in config["behavior"]["hours"]:
        print("doCleaning: Not yet / anymore")
        return False

    if random.randrange(config["behavior"]["chance"]) > 0:
        print("doCleaning: Not now :-(")
        return False

    print("doCleaning: Fuck yeah!")
    return True

# Wann?
#updatetime()

strom = Pin(config["hardware"]["pin"], Pin.OUT)
strom.on()
time.sleep(config["behavior"]["bootOnTime"])
strom.off()

while True:
    if doCleaning():
        strom.on()
        time.sleep(config["behavior"]["onTime"])
        print("main: Thank you for cleaning")
        strom.off()

    time.sleep(config["behavior"]["sleepTime"])
