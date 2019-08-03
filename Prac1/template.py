#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: <Simnikiwe Khonto>
Student Number: <khnsim009>
Prac: <One>
Date: <04/08/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    pass

counter  = 0

def initGPIO():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(11,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(13,GPIO.OUT,initial=GPIO.LOW)
    
    GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(15,GPIO.RISING,callback=increaseButton,bouncetime=300)
    GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(8,GPIO.RISING,callback=decreaseButton,bouncetime=300)


def increaseButton(channel):
    
    global counter    
    counter+=1
    if counter == 8:
        counter = 0
    print(counter)
    counterInbinary = bin(counter)[2:].zfill(3)
    states(counterInbinary[0],counterInbinary[1],counterInbinary[2])

'''def decreaseButton(channel):
    
    global counter
    counter-=1
    if counter < 0:
        counter = 7
    print(counter)    
    counterInbinary = bin(counter)[2:].zfill(3)
    
    states(counterInbinary[0],counterInbinary[1],counterInbinary[2])

def states(led7,led11,led13):
    
    if led7=="1":
        GPIO.output(7,GPIO.HIGH)
    else:
        GPIO.output(7,GPIO.LOW)
    
    if led11=="1":
        GPIO.output(11,GPIO.HIGH)
    else:
        GPIO.output(11,GPIO.LOW)
    
    if led13=="1":
        GPIO.output(13,GPIO.HIGH)
    else:
        GPIO.output(13,GPIO.LOW)'''

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    initGPIO()
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
