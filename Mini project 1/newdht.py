import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
print("Program started")
# read data using pin 14

def get_dht_data():
   instance = dht11.DHT11(pin=12)
   try:
        #while True:
       result = instance.read()
       if result.is_valid():
          print("Last valid input: " + str(datetime.datetime.now()))

          print("Temperature: %-3.1f C" % result.temperature)
          print("Humidity: %-3.1f %%" % result.humidity)
          #return result.temperature, result.humidity
            

   except KeyboardInterrupt:
        print("Cleanup")
        GPIO.cleanup()
