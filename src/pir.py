import RPi.GPIO as GPIO
import os, sys
import signal
import time

if GPIO.RPI_REVISION != 1:
    print("This script is built for model 1 RaspberryPi's")
    sys.exit()

if not os.geteuid()==0:
    print("You must be root to READ or WRITE GPIO pins")
    sys.exit()
s = "Yeah, this is a model %d RaspberryPi!" % (GPIO.RPI_REVISION)
print s
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

GPIO_PIR= 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def notify_movement(channel):
    theTime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    if GPIO.input(GPIO_PIR):
        print('Movement detected on channel %s at [%s]' % (channel, theTime))
    else:
        print('Listening...')

GPIO.add_event_detect(GPIO_PIR, GPIO.BOTH, callback=notify_movement, bouncetime=200)

def cleanup():
    print("\n" + 'bye!')

sys.exitfunc = cleanup

signal.signal(signal.SIGTERM, lambda signum, stack_frame: sys.exit(0))
signal.signal(signal.SIGHUP, lambda signum, stack_frame: sys.exit(0))
signal.signal(signal.SIGQUIT, lambda signum, stack_frame: sys.exit(0))
signal.signal(signal.SIGINT, lambda signum, stack_frame: sys.exit(0))

while 1:
    time.sleep(30)
    continue

