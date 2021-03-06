#!/usr/bin/python  
  
 import RPi.GPIO as GPIO  
 import time    
 import os  
  
 #Set GPIO mode  
 GPIO.setmode(GPIO.BCM)  
  
 #Setup GPIO  
 GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 #GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 #GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 #GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
 #Set up backlight GPIO  
 os.system("sudo sh -c 'echo 508 &gt; /sys/class/gpio/export'")  
  
 #Give the system a quick break  
 time.sleep(0.5)  
  
 #Set the intitial counter value to zero  
 counter = 0 
  
 #var for the 'while' statement to keep it running  
 var = 1 
  
 #Main program  
 while var == 1:  
  if (GPIO.input(23) == False): #Backlight control
  
   if (counter == 0):  
    os.system("sudo sh -c 'echo 'out' &gt; /sys/class/gpio/gpio508/direction'")  
    counter = 1 
    print("counter now 1")  
    time.sleep(0.5)  
  
   elif (counter == 1) or (counter == 3):  
    os.system("sudo sh -c 'echo '1' &gt; /sys/class/gpio/gpio508/value'")  
    counter = 2 
    print("counter now 2")  
    time.sleep(0.5)  
  
   elif (counter == 2):  
    os.system("sudo sh -c 'echo '0' &gt; /sys/class/gpio/gpio508/value'")  
    counter = 3 
    print("counter now 3")  
    time.sleep(0.5)  
  
  #if (GPIO.input(22) == False):  
  # print("22 Working")  
  # time.sleep(0.5)  
  
  #if (GPIO.input(21) == False):  
  # print("27 working")  
  # time.sleep(0.5)  
  
  #if (GPIO.input(18) == False): #Shutdown button  
  # print("SHUTDOWN")  
  # os.system("sudo halt")  
  
 GPIO.cleanup()  
