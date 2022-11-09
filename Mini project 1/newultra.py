import RPi.GPIO as GPIO
import time
import newdht

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN) # echo which is input 
GPIO.setup(5,GPIO.OUT) #trigg which is output
GPIO.setwarnings(False)

def distance_measured():
        GPIO.output(5,GPIO.LOW)
        time.sleep(2)
        GPIO.output(5,GPIO.HIGH)
        time.sleep(0.00001)  # time will be 10 micro sec for default cm valuation
        GPIO.output(5,GPIO.LOW)
        while(GPIO.input(3)==0):
            start=time.time()
        while(GPIO.input(3)==1):
            end=time.time()
        duration=end-start
        distance=duration*17150   #17150 is pulse duration for 10micro sec.
        distance=round(distance,3)
        return distance

try:
    while True:
        #print(ins)
        distance1=distance_measured()
        time.sleep(2)
        distance2=distance_measured()
        diff=distance1-distance2
        if(distance2<distance1):
            print("rain is falling! ",distance2*10," mm")
            time.sleep(1)
            ins=newdht.get_dht_data()
        else:
            print("Rain is stopped")
            print("rain measured is: ",distance2*10," mm")
            time.sleep(1)
            ins=newdht.get_dht_data()  
except KeyboardInterrupt:
    GPIO.cleanup()
