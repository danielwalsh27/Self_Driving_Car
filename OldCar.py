#Importing Libraries
#https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051
import RPi.GPIO as GPIO
import sys
import time

# Initializing all variables
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
dc_M = 0
dc_S = 0

# Setup for motor
MotorA = 36
MotorB = 38
MotorE = 40
GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorE,GPIO.OUT)
motor_A = GPIO.PWM(MotorA,100)
motor_B = GPIO.PWM(MotorB,100)
motor_E = GPIO.PWM(MotorE,100)
motor_A.start(dc_M)
motor_B.start(dc_M)
motor_E.start(dc_M)

# Setup for steering
SteerA = 37
SteerB = 35
SteerE = 33
GPIO.setup(SteerA,GPIO.OUT)
GPIO.setup(SteerB,GPIO.OUT)
GPIO.setup(SteerE,GPIO.OUT)
steer_A = GPIO.PWM(SteerA,100)
steer_B = GPIO.PWM(SteerB,100)
steer_E = GPIO.PWM(SteerE,100)
steer_A.start(dc_S)
steer_B.start(dc_S)
steer_E.start(dc_S)

# Setup for Ultra-Sonic Sensor(s)
trig = 7
echo = 32
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

# Setup for headlights/taillights
headlights = 8
taillight = "XXXXX"
GPIO.setup(headlights,GPIO.OUT)
#GPIO.setup(taillight,GPIO.OUT)

# Function Defintions 
def forward (speed):
    #print ("Forward : ", speed, " direction: Straight")
    motor_A.ChangeDutyCycle(0)
    motor_B.ChangeDutyCycle(speed)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(0)
    steer_B.ChangeDutyCycle(0)
    steer_E.ChangeDutyCycle(0)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.LOW)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)

def forward_Left (speed,draw):
    #print ("Forward: ", speed, " draw Left of ", draw)
    motor_A.ChangeDutyCycle(0)
    motor_B.ChangeDutyCycle(speed)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(0)
    steer_B.ChangeDutyCycle(draw) #70
    steer_E.ChangeDutyCycle(draw)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)

def forward_Right (speed,draw):
    #print ("Forward: ", speed, " draw Right of ", draw)
    motor_A.ChangeDutyCycle(0)
    motor_B.ChangeDutyCycle(speed)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(draw)
    steer_B.ChangeDutyCycle(0)
    steer_E.ChangeDutyCycle(draw)
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)

def back (speed):
    #print ("Back: ", dc_M, " direction: Straight")
    motor_A.ChangeDutyCycle(speed)
    motor_B.ChangeDutyCycle(0)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(0)
    steer_B.ChangeDutyCycle(0)
    steer_E.ChangeDutyCycle(0)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.LOW)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)

def back_Left (speed,draw):
    #print ("Back: ", speed, " draw Left of ", draw)
    motor_A.ChangeDutyCycle(speed)
    motor_B.ChangeDutyCycle(0)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(0)
    steer_B.ChangeDutyCycle(draw)
    steer_E.ChangeDutyCycle(draw)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)

def back_Right (speed,draw):
    #print ("Back: ", speed, " draw Right of ", draw)
    motor_A.ChangeDutyCycle(speed)
    motor_B.ChangeDutyCycle(0)
    motor_E.ChangeDutyCycle(speed)
    steer_A.ChangeDutyCycle(draw)
    steer_B.ChangeDutyCycle(0)
    steer_E.ChangeDutyCycle(draw)
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)

def move_45_Left ():
    back_Right(100,100);    time.sleep(.4)
    forward_Left(100,100);  time.sleep(.5)
    back_Right(100,100);    time.sleep(.5)
    forward_Left(100,100);  time.sleep(.6)
    forward(0)

def move_45_Right ():   
    back_Left(100,100);     time.sleep(.4)
    forward_Right(100,100); time.sleep(.5)
    back_Left(100,100);     time.sleep(.5)
    forward_Right(100,100); time.sleep(.6)
    forward(0)

def move_90_Left ():
    back_Right(100,100);    time.sleep(.6)
    forward_Left(100,100);  time.sleep(.8)
    back_Right(100,100);    time.sleep(.8)
    forward_Left(100,100);  time.sleep(.8)
    back_Right(100,100);    time.sleep(.7)
    forward(80);            time.sleep(.5)
    forward(0)

def move_90_Right ():
    back_Left(100,100);     time.sleep(.6)
    forward_Right(100,100); time.sleep(.8)
    back_Left(100,100);     time.sleep(.8)
    forward_Right(100,100); time.sleep(.8)
    back_Left(100,100);     time.sleep(.7)
    forward(80);            time.sleep(.5)
    forward(0)

        
def controlCar ():
    print ("User Control")
    slo = 30
    med = 50
    fo_ = 70
    fas = 99
    while True:
        t = 0
        c = sys.stdin.read(1)
        if c == '1':
            GPIO.output(headlights,True)
        if c == '2':
            GPIO.output(headlights,False)
        if c == 'w':
            forward(fo_); time.sleep(t)
        if c == 'a':
            forward_Left(fo_,60); time.sleep(t)
        if c == 's':
            back(60); time.sleep(t)
        if c == 'd':
            forward_Right(fo_,60); time.sleep(t)
        if c == 'b':
            forward_Left(slo,70); time.sleep(t)
        if c == 'n':
            forward(slo); time.sleep(t)
        if c == 'm':
            forward_Right(slo,70); time.sleep(t)
        if c == 'j':
            forward_Left(med,60); time.sleep(t)
        if c == 'k':
            forward(med); time.sleep(t)
        if c == 'l':
            forward_Right(med,60); time.sleep(t)
        if c == 'i':
            forward_Left(fas,60); time.sleep(t)
        if c == 'o':
            forward(fas); time.sleep(t)
        if c == 'p':
            forward_Right(fas,60); time.sleep(t)
        if c == 'c':
            print ("Enter Speed:")
            spd = sys.stdin.read(4)
            print ("L/R/S ?")
            dirc = sys.stdin.read(1)
            if dirc == 'L':
                forward_Left(spd,70)
            if dirc == 'R':
                forward_Right(spd,70)
            if dirc == 'S':
                forward(spd) 
        if c == ' ':
            forward(0)
        if c == 'q':
            break
        if c == 'h':
            print ("w = Forward(",fo_,")"); print ("a = F_Left (",fo_,")")
            print ("d = F_Rght (",fo_,")"); print ("s = F_Back ( 60 )")
            print ("b = F_Left (",slo,")"); print ("n = Forward(",slo,")")
            print ("m = F_Rght (",slo,")"); print ("j = F_Left (",med,")")
            print ("k = Forward(",med,")"); print ("l = F_Rght (",med,")")
            print ("i = F_Left (",fas,")"); print ("o = Forward(",fas,")")
            print ("p = F_Rght (",fas,")")

# ******************************( *MAIN* )******************************

controlCar()

goLeft = False
go_45 = True
while True:
    GPIO.output(trig,False)
    time.sleep(.05)
    GPIO.output(trig,True)
    time.sleep(.05)
    GPIO.output(trig,False)
    start = time.time()
    #end = time.time()
    while (GPIO.input(echo) == 0):
        start = time.time()
    while (GPIO.input(echo) == 1):
        end = time.time()
    duration = end - start
    distance = duration * 17150
    distance = round(distance,2)
    print ("Distance: ", distance, " cm.")

    #c = sys.stdin.read(1)
    #if c == '':
    #    continue
    #if c == 'q':
    #    break
    if(distance > 250):
        forward(90)
    if(distance > 200 and distance < 250):
        forward(85)
    if(distance > 120 and distance < 200):
        forward(75)
    if(distance > 60 and distance < 120):
        forward(60)
    if(distance > 40 and distance < 60):
        forward(50)
    if(distance > 15 and distance < 40):
        forward(40)
    if(distance < 15):
        print ("Changing course")
        back(50);   time.sleep(1)
        if(goLeft):                 #
            if(go_45):              # called by TF
                move_45_Left()      #
                goLeft = False      #
                go_45 = False       #
            else:                   # called by FT
                move_90_Left()      #
                goLeft = True       #
                go_45 = True        #
        else:                       #
            if(go_45):              #called init/ FF
                move_45_Right()     #
                goLeft = True       #
                go_45 = False       #
            else:                   # called by TT
                move_90_Right()     #
                goLeft = False      #
                go_45 = True        #

GPIO.cleanup()
