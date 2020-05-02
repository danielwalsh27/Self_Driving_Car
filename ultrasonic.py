import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
listy = [3,5,7,8,10,11]
led1 = 3
led2 = 5
led3 = 7
led4 = 8
led5 = 10
led6 = 11
trig = 40 
echo = 38
gpio.setup(listy,gpio.OUT)
gpio.setup(led1,gpio.OUT)
gpio.setup(led2,gpio.OUT)
gpio.setup(led3,gpio.OUT)
gpio.setup(led4,gpio.OUT)
gpio.setup(led5,gpio.OUT)
gpio.setup(led6,gpio.OUT)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

count = 0
while(True):
##    
    count = count + 1
    if(count % 100 == 0):
        time.sleep(10)
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
    print "Distance:", distance, "cm     ", count

    if(distance > 50):
        gpio.output(led1,False)
        gpio.output(led2,False)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        gpio.output(led6,False)
    if(distance > 45 and distance < 50):
        gpio.output(led1,True)
        gpio.output(led2,False)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        gpio.output(led6,False)
    if(distance > 28 and distance < 35):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,False)
        gpio.output(led4,False)
        gpio.output(led5,False)
        gpio.output(led6,False)
    if(distance > 20 and distance < 28):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,False)
        gpio.output(led5,False)
        gpio.output(led6,False)
    if(distance > 12 and distance < 20):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,True)
        gpio.output(led5,False)
        gpio.output(led6,False)
    if(distance > 7 and distance < 12):
        gpio.output(led1,True)
        gpio.output(led2,True)
        gpio.output(led3,True)
        gpio.output(led4,True)
        gpio.output(led5,True)
        gpio.output(led6,False)
    if(distance < 7):
        for i in listy:
            gpio.output(i,True)
    
    
