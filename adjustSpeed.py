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

sleep(2)

print ("Moving Backwards & Turn Right")
GPIO.output(MotorA,GPIO.HIGH)
GPIO.output(MotorB,GPIO.LOW)
GPIO.output(MotorE,GPIO.HIGH)
GPIO.output(SteerA,GPIO.HIGH)
GPIO.output(SteerB,GPIO.LOW)
GPIO.output(SteerE,GPIO.HIGH)
 
sleep(2)
 
print ("Stopping motor")
GPIO.output(MotorE,GPIO.LOW)
GPIO.output(SteerE,GPIO.LOW)

print ("PWM test")
GPIO.output(MotorE,GPIO.HIGH)
pwm1 = GPIO.PWM(MotorA,100)
pwm2 = GPIO.PWM(MotorB,100)
pwm3 = GPIO.PWM(MotorE,100)
dc = 0
pwm1.start(dc)
pwm2.start(dc)
pwm3.start(dc)

dc = 30
print ("PWM speed of: ", dc)
pwm1.ChangeDutyCycle(dc)
pwm2.ChangeDutyCycle(dc)
pwm3.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)

sleep (3)

dc = 80
print ("PWM speed of: ", dc)
pwm1.ChangeDutyCycle(dc)
pwm2.ChangeDutyCycle(dc)
pwm3.ChangeDutyCycle(dc)
GPIO.output(MotorA,GPIO.LOW)
GPIO.output(MotorB,GPIO.HIGH)
GPIO.output(MotorE,GPIO.HIGH)

sleep (6)
while True:
      for dc in range(50, 60, 1):    # Loop 0 to 100 stepping dc by 5 each loop
            print ("PWM speed of: ", dc)
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            pwm3.ChangeDutyCycle(dc)
            GPIO.output(MotorA,GPIO.LOW)
            GPIO.output(MotorB,GPIO.HIGH)
            GPIO.output(MotorE,GPIO.HIGH)
            sleep (3)

      for dc in range(65, 85, 1):    # Loop 0 to 100 stepping dc by 5 each loop
            print ("PWM speed of: ", dc)
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            pwm3.ChangeDutyCycle(dc)
            GPIO.output(MotorA,GPIO.LOW)
            GPIO.output(MotorB,GPIO.HIGH)
            GPIO.output(MotorE,GPIO.HIGH)
            sleep (2)



 
GPIO.cleanup()
