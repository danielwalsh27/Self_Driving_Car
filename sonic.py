import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
trig = 7 
echo = 32
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

while(True):
    gpio.output(trig,False)
    time.sleep(.05)
    gpio.output(trig,True)
    time.sleep(.05)
    gpio.output(trig,False)
    start = time.time()
    #end = time.time()
    while (gpio.input(echo) == 0):
        start = time.time()
    while (gpio.input(echo) == 1):
        end = time.time()
    duration = end - start
    distance = duration * 17150
    distance = round(distance,2)
    print ("Distance:", distance, "cm     ")
