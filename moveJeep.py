#Importing Libraries
#https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
import RPi.GPIO as GPIO
import time
import sys

# Initializing all variables
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setup for Lights
headlights = 38
taillights = 40
GPIO.setup(headlights,GPIO.OUT)
GPIO.setup(taillights,GPIO.OUT)

# Setup for Left
LeftA = 13
LeftB = 15
LeftE = 11
GPIO.setup(LeftA,GPIO.OUT)
GPIO.setup(LeftB,GPIO.OUT)
GPIO.setup(LeftE,GPIO.OUT)

# Setup forRight
RightA = 16
RightB = 18
RightE = 22
GPIO.setup(RightA,GPIO.OUT)
GPIO.setup(RightB,GPIO.OUT)
GPIO.setup(RightE,GPIO.OUT)

def stop():
    GPIO.output(LeftE,False)
    GPIO.output(RightE,False)

# Function Defintions 
def forward ():
    GPIO.output(taillights,False)
    print ("Forward  ")
    GPIO.output(LeftA,False)
    GPIO.output(LeftB,True)
    GPIO.output(LeftE,True)
    GPIO.output(RightA,False)
    GPIO.output(RightB,True)
    GPIO.output(RightE,True)
    GPIO.output(taillights,True)

def left (t):
    GPIO.output(taillights,False)
    print ("Left  ")
    GPIO.output(LeftA,True)
    GPIO.output(LeftB,False)
    GPIO.output(LeftE,True)
    GPIO.output(RightA,False)
    GPIO.output(RightB,True) 
    GPIO.output(RightE,True)
    time.sleep(t)
    GPIO.output(taillights,True)

def right (t):
    GPIO.output(taillights,False)
    print ("Right  ")
    GPIO.output(LeftA,False)
    GPIO.output(LeftB,True)
    GPIO.output(LeftE,True)
    GPIO.output(RightA,True)
    GPIO.output(RightB,False)
    GPIO.output(RightE,True)
    time.sleep(t)
    GPIO.output(taillights,True)

def back ():
    GPIO.output(taillights,False)
    print ("Back ")
    GPIO.output(LeftA,GPIO.HIGH)
    GPIO.output(LeftB,GPIO.LOW)
    GPIO.output(LeftE,GPIO.HIGH)
    GPIO.output(RightA,GPIO.HIGH)
    GPIO.output(RightB,GPIO.LOW)
    GPIO.output(RightE,GPIO.HIGH)
    GPIO.output(taillights,True)

def controlCar ():
    print ("User Control")
    med = 50
    fas = 99
    while True:
        t = 0
        c = sys.stdin.read(1)
        if c == '1':
            GPIO.output(headlights,True)
        if c == '2':
            GPIO.output(headlights,False)
        if c == '9':
            GPIO.output(taillights,True)
        if c == '0':
            GPIO.output(taillights,False)
        if c == 'w':
            forward();   time.sleep(t)
        if c == 'a':
            left(1);     time.sleep(t)
        if c == 's':
            back();      time.sleep(t)
        if c == 'd':
            right(1);    time.sleep(t)
        if c == ' ':
            stop()
        if c == 'q':
            break
        if c == 'h':
            print ("w = Forward()"); print ("a = Left()")
            print ("d = Right()");   print ("s = Back()")
            print ("1/2 = headlights");print ("9/0 = taillights");
            print ("q = quit ") ;

# ******************************( *MAIN* )*****************************
controlCar()




GPIO.cleanup()
