import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

moisture_channel = 17
pump_channel = 27
pump_duration = 60
moisty_val = 20000

adc = Adafruit_ADS1x15.ADS1115()

def runPump():
    print("running pump")
    GPIO.output(pump_channel, GPIO.LOW)
    time.sleep(pump_duration)

print("--- " + time.ctime())

GPIO.setmode(GPIO.BCM)

GPIO.setup(moisture_channel, GPIO.IN)
GPIO.setup(pump_channel, GPIO.OUT)

result = adc.read_adc(0, gain=1)
print(result)
if result > moisty_val:
    print("low water")
    runPump()
else:
    print("water is great")


GPIO.cleanup()


