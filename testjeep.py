import RPi.GPIO as GPIO
from time import sleep
import sys
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 13
Motor1B = 15
Motor1E = 11
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
CL_A = GPIO.PWM(Motor1A,100)
CL_B = GPIO.PWM(Motor1B,100)
CL_E = GPIO.PWM(Motor1E,100)
CL_A.start(100)
CL_B.start(100)
CL_E.start(100)

RightA = 16
RightB = 18
RightE = 22
GPIO.setup(RightA,GPIO.OUT)
GPIO.setup(RightB,GPIO.OUT)
GPIO.setup(RightE,GPIO.OUT)
CR_A = GPIO.PWM(RightA,100)
CR_B = GPIO.PWM(RightB,100)
CR_E = GPIO.PWM(RightE,100)
CR_A.start(100)
CR_B.start(100)
CR_E.start(100)

print ("Turning motor on")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
#BACK
GPIO.output(RightA,GPIO.HIGH)
GPIO.output(RightB,GPIO.LOW)
GPIO.output(RightE,GPIO.HIGH)
 
sleep(2)
 
print ("Stopping motor")
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(RightE,GPIO.LOW)
 
GPIO.cleanup()
