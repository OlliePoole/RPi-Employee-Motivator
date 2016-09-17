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

ZAP_ONE = 2
ZAP_TWO = 3

print("LED - Setup complete")

app = Flask(__name__)

def reset():
    GPIO.setup(LED_RED_ONE, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_GREEN_ONE, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_BLUE_ONE, GPIO.OUT, initial= GPIO.LOW)

    GPIO.setup(LED_RED_TWO, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_GREEN_TWO, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_BLUE_TWO, GPIO.OUT, initial= GPIO.LOW)

    GPIO.setup(LED_RED_THREE, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_GREEN_THREE, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(LED_BLUE_THREE, GPIO.OUT, initial= GPIO.LOW)

    GPIO.setup(ZAP_ONE, GPIO.OUT, initial= GPIO.LOW)
    GPIO.setup(ZAP_TWO, GPIO.OUT, initial= GPIO.LOW)

@app.route('/')
def index():
    reset()
    return "Hello World"

@app.route('/zap')
def zap():
    GPIO.output(ZAP_ONE, GPIO.HIGH)
    GPIO.output(ZAP_TWO, GPIO.HIGH)

    return "Zap complete"

@app.route('/start')
def start():
    GPIO.output(LED_GREEN_ONE, GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(LED_GREEN_TWO, GPIO.HIGH)
    time.sleep(2)
    
    GPIO.output(LED_GREEN_THREE, GPIO.HIGH)
    time.sleep(2)

    return "start-complete"

@app.route('/mild')
def mild():
    reset()

    GPIO.output(LED_RED_ONE, GPIO.HIGH)
    time.sleep(2)
    
    reset()

    return "mild-shock-complete"

@app.route('/medium')
def medium():
    reset()
  
    GPIO.output(LED_RED_ONE, GPIO.HIGH)
    time.sleep(2)

    GPIO.output(LED_RED_TWO, GPIO.HIGH)
    time.sleep(2)

    reset()

    return "medium-shock-complete"

@app.route('/harsh')
def harsh():
    reset()

    GPIO.output(LED_RED_ONE, GPIO.HIGH)
    time.sleep(2)

    GPIO.output(LED_RED_TWO, GPIO.HIGH)
    time.sleep(2)

    GPIO.output(LED_RED_THREE, GPIO.HIGH)
    time.sleep(2)

    reset()

    return "harsh-shock-complete"

@app.route('/red')
def red():
    GPIO.output(LED_RED_ONE, GPIO.HIGH)
    GPIO.output(LED_GREEN_ONE, GPIO.LOW)
    GPIO.output(LED_BLUE_ONE, GPIO.LOW)
    return "RED ON"

@app.route('/green')
def green():
    GPIO.output(LED_RED_ONE, GPIO.LOW)
    GPIO.output(LED_BLUE_ONE, GPIO.LOW)
    GPIO.output(LED_GREEN_ONE, GPIO.HIGH)
    return "GREEN ON"

@app.route('/blue')
def blue():
    GPIO.output(LED_GREEN_ONE, GPIO.LOW)
    GPIO.output(LED_RED_ONE, GPIO.LOW)
    GPIO.output(LED_BLUE_ONE, GPIO.HIGH)
    return "BLUE ON"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
