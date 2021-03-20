# CamJam Edukit 2 - Sensors
# Worksheet 2 - LEDs and Buzzer
# Edited by @L_S_Security to make a little times tables game for primary school age children

# Import Python libraries
import RPi.GPIO as GPIO
import time
from random import *

# Change this array to add more times tables to test on, eg:
tables=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#tables=[5, 2, 10, 4]
correct=0

# How many questions to ask
questions=10

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the three GPIO pins for Output
GPIO.setup(18, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


for i in range(10):
    GPIO.output(18, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

    operand=tables[randint(0,len(tables)-1)]
    exponent=randint(1,12)
    answer = input("What is "+str(operand)+"*"+str(exponent)+"? ")

    result=operand*exponent

    if (result==int(answer)):
        print("CORRECTAMUNDO!!!")
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(2)
        correct=correct+1
    else:
        print("INCORRECT!!!")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(5)

print("You got "+str(correct)+" correct answers!! Well done!")

GPIO.output(18, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

GPIO.cleanup()
