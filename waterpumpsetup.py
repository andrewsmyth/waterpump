import RPi.GPIO as GPIO
import time

moisture_channel = 17
pump_channel = 27
pump_duration = 60

def runPump():
    print("running pump")
    GPIO.output(pump_channel, GPIO.LOW)
    time.sleep(pump_duration)

print("--- " + time.ctime())

GPIO.setmode(GPIO.BCM)

GPIO.setup(moisture_channel, GPIO.IN)
GPIO.setup(pump_channel, GPIO.OUT)

result = GPIO.input(moisture_channel)

if result is 1:
    print("low water")
    runPump()
else:
    print("water is great")


GPIO.cleanup()


