import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

state = False

for number in range(0,10):
	GPIO.output(11,state)
	print("state=%s"% state)
	time.sleep(5)
	state = not state

GPIO.cleanup()
