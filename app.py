from flask import Flask

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_RED_ONE = 4
LED_GREEN_ONE = 5
LED_BLUE_ONE = 6

LED_RED_TWO = 23
LED_GREEN_TWO = 24
LED_BLUE_TWO = 25

LED_RED_THREE = 20
LED_GREEN_THREE = 21
LED_BLUE_THREE = 22

GPIO.setup(LED_RED_ONE, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN_ONE, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_BLUE_ONE, GPIO.OUT, initial= GPIO.LOW)

GPIO.setup(LED_RED_TWO, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN_TWO, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_BLUE_TWO, GPIO.OUT, initial= GPIO.LOW)

GPIO.setup(LED_RED_THREE, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN_THREE, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_BLUE_THREE, GPIO.OUT, initial= GPIO.LOW)

GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def onClick(null):
    print("Button Clicked")

GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=onClick, bouncetime=100) 

print("LED - Setup complete")

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/red')
def red():
    GPIO.output(LED_RED, GPIO.HIGH)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)
    return "RED ON"

@app.route('/green')
def green():
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.HIGH)
    return "GREEN ON"

@app.route('/blue')
def blue():
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.HIGH)
    return "BLUE ON"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
