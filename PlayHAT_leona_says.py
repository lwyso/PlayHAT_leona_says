## LEONA SAYS

## 2 player game - Player 1 will press a sequence of buttons
## and set i action a sequence of lights.
## Player 2 observes the light sequence then attempts
## to copy the sequence by pressing buttons
## If correct a celebratory sequnce of lights plays
## otherwise the buzzer sounds.

## To set up PlayHAT, please visit https://github.com/4tronix/PlayHAT

import time
from neopixel import *
from gpiozero import Button, Buzzer
from signal import pause

btnG = Button(17)
btnR = Button(4)
btnB = Button(22)

btnY = Button(27)

beeper = Buzzer(23)

MyList = []
MyCheckList = []

# LED strip configuration:
LED_COUNT      = 9       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=30, iterations=5):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

def Play(MyList):
    for item in MyList:
        if item == 'green':
            for i in range(255,0,-125):
                colorWipe(strip, Color(i,0,0))                
        if item == 'red':
            for i in range(255,0,-125):
                colorWipe(strip, Color(0,i,0))
                
        if item == 'blue':
            for i in range(255,0,-125):
                colorWipe(strip, Color(0,0,i)) 

def btnGpressed():
##    print('green pressed')
    MyList.append('green')

def btnRpressed():
##    print('red pressed')
    MyList.append('red')
    
def btnBpressed():
##    print('blue pressed')
    MyList.append('blue')

## For MyCheckList

def btnGpressedAgain():
    print('green pressed')
    MyCheckList.append('green')

def btnRpressedAgain():
    print('red pressed')
    MyCheckList.append('red')
    
def btnBpressedAgain():
    print('blue pressed')
    MyCheckList.append('blue')

def btnYpressedAgain():
    global finished
    print('Player 1 sequence: ',MyList)
    print('Player 2 guessed: ',MyCheckList)
    if MyList == MyCheckList:
        print('Well done!')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
                
    else:
        print('Sorry, better luck next time!')
        colorWipe(strip, Color(0, 255, 0))
        beeper.on()

    colorWipe(strip, Color(0, 0, 0))
    beeper.off()
    finished = True
    
## The game begin!    

def btnYpressed():
    global finished
##    print(MyList)
    Play(MyList)
    
    # Theater chase animations.
    theaterChase(strip, Color(127, 127, 127))  # White theater chase
    theaterChase(strip, Color(127,   0,   0))  # Red theater chase
    theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
    colorWipe(strip, Color(0, 0, 0))
    
    btnG.when_pressed = btnGpressedAgain
    btnR.when_pressed = btnRpressedAgain
    btnB.when_pressed = btnBpressedAgain
    btnY.when_pressed = btnYpressedAgain

btnG.when_pressed = btnGpressed
btnR.when_pressed = btnRpressed
btnB.when_pressed = btnBpressed
btnY.when_pressed = btnYpressed
finished = False
while not finished:
    pass