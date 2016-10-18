


import RPi.GPIO as GPIO
import time

#led_pin defines the pin number connected to LED 
led_pin = 38
m_sensor = 35


GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(m_sensor, GPIO.IN)

while True:
	i=GPIO.input(35)
	if i==0:

		print ("no intruder"),i
		GPIO.output(38, 0)
		time.sleep(0.1)
	
	elif i==1:
		print("intruder")
		GPIO.output(led_pin,True)
		time.sleep(1)
		GPIO.output(led_pin,False)
		GPIO.cleanup 		

		
