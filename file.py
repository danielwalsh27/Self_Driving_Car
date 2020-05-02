import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

light = [37, 36, 38, 40, 32, 31, 12]
lght = [12, 31, 32, 40, 38, 36, 37]
cops = [12,31,32,40,40,32,31,12]
mix = [32,38,12,40,36,31,37,38,40,12,36,32,37]
button = 33
but2 = 15

gpio.setmode(gpio.BOARD)
gpio.setup(light,gpio.OUT)
gpio.setup(lght,gpio.OUT)
gpio.setup(cops,gpio.OUT)
gpio.setup(mix,gpio.OUT)
gpio.setup(button,gpio.IN)
gpio.setup(but2,gpio.IN)

while True:
    buttonp = gpio.input(button)
    twop = gpio.input(but2)
    if(twop == True):
        for t in cops:
            gpio.output(t,True) 
            time.sleep(.03)
            gpio.output(t,False)
            time.sleep(.01)
    if(twop == False):
        for l in mix:
            gpio.output(l,True)
            time.sleep(.39)
        for k in mix:
            gpio.output(k,True)
            time.sleep(.1)
            gpio.output(k,False)
            time.sleep(.12)
        for l in mix:
            gpio.output(l,True)
            time.sleep(.1)
        for k in mix:
            gpio.output(k,True)
            time.sleep(.1)
            gpio.output(k,False)
            time.sleep(.36)
    if(buttonp == True):
        for t in cops:
            gpio.output(t,True) 
            time.sleep(.02)
            gpio.output(t,False)
            time.sleep(.00)
    if(buttonp == False):
        for l in lght:
            gpio.output(l,True)
            time.sleep(.1)
        for i in light:
            gpio.output(i,False)
            time.sleep(.15)
        for l in lght:
            gpio.output(l,True)
            time.sleep(.27)
            gpio.output(l,False)
            time.sleep(.17)
        for k in light:
            gpio.output(k,True)
            time.sleep(.15)
            gpio.output(k,False)
            time.sleep(.25)


 
            

      
