#importing libraries, setting up board
import RPi.GPIO as GPIO
from pynput.keyboard import Key, Listener
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#setup Motors
MotorA = 16
MotorB = 18
MotorE = 22
GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorE,GPIO.OUT)

#setup Steering
SteerA = 15
SteerB = 13
SteerE = 11
GPIO.setup(SteerA,GPIO.OUT)
GPIO.setup(SteerB,GPIO.OUT)
GPIO.setup(SteerE,GPIO.OUT)

#setup Ultrasonic sensor
trig = 40 
echo = 38
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

#setup PWM 
pwm=GPIO.PWM(MotorE,100)
pwm.start(0)

def f_left(speed,delay):
    print("Forward left")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def b_left(speed,delay):
    print("Back left")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def f_right(speed,delay):
    print("Forward right")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def b_right(speed,delay):
    print("Back right")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(delay)

def forward(speed,delay):
    print("Forward")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.LOW)
    time.sleep(delay)
    
    
def back(speed,delay):
    print("Back")
    pwm.ChangeDutyCycle(speed)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.LOW)
    time.sleep(delay)

switch = 0
count = 0
maxIts = 500
while(False):
    count = count + 1
    if(count > maxIts): break
    
    GPIO.output(trig,False)
    time.sleep(.05)
    GPIO.output(trig,True)
    time.sleep(.05)
    GPIO.output(trig,False)

    #start = time.time()
    #end = time.time()
    while (GPIO.input(echo) == 0):
        start = time.time()
    while (GPIO.input(echo) == 1):
        end = time.time()
    duration = end - start
    distance = duration * 17150  * 0.393701
    distance = round(distance,2)
    print ("Distance:", distance, "in")

    if(distance < 15):
        if(switch == 0):
            b_left(75,2.00)
            switch = 1;
        elif(switch == 1):
            b_right(75,2.00)
            switch = 2;
        elif(switch == 2):
            b_left(75,2.00)
            switch = 3;
        else:
            b_right(75,2.00)
            switch = 0;
        
    elif (distance > 15):
        if(distance > 100):
            forward(80,0)
        elif(distance < 40 and distance > 15):
            forward(60,0)
        else:
            forward(70,0)

forward(0,0)



print("User Control")

def on_press(key):
    #print('{0} pressed'.format(key))
    if key == Key.esc:
        return False    # Stop listener
    elif key == Key.down:
        print("Stop")
        forward(0,0)
    elif key == Key.up:
        print("Up")
        forward(100,0)
    elif key == Key.left:
        print("Left")
        f_left(100,0)
    elif key == Key.right:
        print("Right")
        f_right(100,0)
    elif key == Key.space:
        print("Backwards")
        back(100,0)
    #forward(0,0)



def on_press(key):
    print('{0} pressed'.format(key))
    if key == Key.down:
        print("Backwards")
        back(100,0)
    elif key == Key.up:
        print("Up")
        forward(100,0)
    elif key == Key.left:
        print("Left")
        f_left(100,0)
    elif key == Key.right:
        print("Right")
        f_right(100,0)


def on_release(key):
    print('{0} release'.format(key))
    forward(0,0)
    if key == Key.esc:
        return False # Stop listener

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


    
            
print("End Program")
pwm.stop()
GPIO.cleanup()
