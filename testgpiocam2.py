import RPi.GPIO as GPIO
import time
import os

from datetime import datetime



#led_pin defines the pin number connected to LED 

m_sensor = 8


GPIO.setmode(GPIO.BOARD)

GPIO.setup(m_sensor, GPIO.IN)

i = 0


while True:
	i=GPIO.input(8)
	if i==0:

		print ("no intruder")
		
		time.sleep(1)
	
	elif i==1:
		t= "{:%m%d%Y%H%M%S}".format(datetime.now())
			
		

		print("intruder"+t)
		
		os.system('fswebcam -r 960x720 /home/pi/security/'+t +'.jpg' )
		
		os.system('echo "image has been saved to http://www.lwaldtech.com" | mail -s "motion detected" email1@gmail.com, email2@gmail.com, user@email.com')
		time.sleep(60)
		
		GPIO.cleanup 		

		
