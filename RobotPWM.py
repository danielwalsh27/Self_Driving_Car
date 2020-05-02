import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
MotorA = 16
MotorB = 18
MotorE = 22
SteerA = 15
SteerB = 13
SteerE = 11
GPIO.setup(MotorA,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorE,GPIO.OUT)
GPIO.setup(SteerA,GPIO.OUT)
GPIO.setup(SteerB,GPIO.OUT)
GPIO.setup(SteerE,GPIO.OUT)

print ("Moving Forwards & Turn Left")
GPIO.output(MotorA,False)
GPIO.output(MotorB,True)
GPIO.output(MotorE,True)
GPIO.output(SteerA,False)
GPIO.output(SteerB,True)
GPIO.output(SteerE,True)
sleep(4)

print ("Moving Backwards & Turn Right")
GPIO.output(MotorA,GPIO.HIGH)
GPIO.output(MotorB,GPIO.LOW)
GPIO.output(MotorE,GPIO.HIGH)
GPIO.output(SteerA,GPIO.HIGH)
GPIO.output(SteerB,GPIO.LOW)
GPIO.output(SteerE,GPIO.HIGH)
sleep(4)
 
print ("Stopping motor")
GPIO.output(MotorE,GPIO.LOW)
GPIO.output(SteerE,GPIO.LOW)
sleep(1)

print ("PWM test")
GPIO.output(MotorE,GPIO.HIGH)
pwm = GPIO.PWM(MotorE,100)
pwm3.start(0)

dc = 56
print ("PWM speed of: ", dc)
pwm.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)

sleep (3)

dc = 77
print ("PWM speed of: ", dc)
pwm.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)

sleep (6)
for dc in range(50, 60, 1):    # Loop 0 to 100 stepping dc by 5 each loop
      print ("PWM speed of: ", dc)
      pwm.ChangeDutyCycle(dc)
      GPIO.output(MotorA,GPIO.LOW)
      GPIO.output(MotorB,GPIO.HIGH)
      GPIO.output(MotorE,GPIO.HIGH)
      sleep (2)

for dc in range(75, 85, 1):    # Loop 0 to 100 stepping dc by 5 each loop
      print ("PWM speed of: ", dc)
      pwm.ChangeDutyCycle(dc)
      GPIO.output(MotorA,GPIO.LOW)
      GPIO.output(MotorB,GPIO.HIGH)
      GPIO.output(MotorE,GPIO.HIGH)
      sleep (2)
      
while(False):
    print ("Moving Forwards & Turn Left")
    GPIO.output(MotorA,GPIO.LOW)
    GPIO.output(MotorB,GPIO.HIGH)
    GPIO.output(MotorE,GPIO.HIGH)
    GPIO.output(SteerA,GPIO.LOW)
    GPIO.output(SteerB,GPIO.HIGH)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(.3)

    print ("Moving Backwards & Turn Right")
    GPIO.output(MotorA,GPIO.HIGH)
    GPIO.output(MotorB,GPIO.LOW)
    GPIO.output(MotorE,GPIO.LOW)
    GPIO.output(SteerA,GPIO.HIGH)
    GPIO.output(SteerB,GPIO.LOW)
    GPIO.output(SteerE,GPIO.HIGH)
    time.sleep(.3)
     
    print ("Stopping motor")
    pwm.ChangeDutyCycle(0)
    GPIO.output(MotorE,GPIO.LOW)
    GPIO.output(SteerE,GPIO.LOW)
    time.sleep(2)

while(False):
    for dc in range(28, 29, 1):    # Loop 0 to 100 stepping dc by 5 each loop
        print ("PWM speed of: ", dc)
        pwm.ChangeDutyCycle(dc)
        GPIO.output(MotorA,GPIO.LOW)
        GPIO.output(MotorB,GPIO.HIGH)
        GPIO.output(MotorE,GPIO.HIGH)
        time.sleep (.5)

    for dc in range(55, 57, 1):    # Loop 0 to 100 stepping dc by 5 each loop
        print ("PWM speed of: ", dc)
        pwm.ChangeDutyCycle(dc)
        GPIO.output(MotorA,GPIO.LOW)
        GPIO.output(MotorB,GPIO.HIGH)
        GPIO.output(MotorE,GPIO.HIGH)
        time.sleep (.5)





pwm.stop() 
GPIO.cleanup()
