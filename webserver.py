import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
intCount = 0
intCountDownStart = 0

@app.route('/')
def index():

    return render_template('index2.html')

@app.route('/increasebutton/')

def variable6():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    global intCount
    intCount = intCount + 1
    intCountLight = intCount
    templateData = {
        'currentCount' : intCountLight
        }
    if(intCountLight >= 16):
        intCountLight = intCountLight - 16
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.5)
    elif(intCountLight <= 16):
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 8):
        intCountLight = intCountLight - 8
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight <= 8):
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 4):
        intCountLight = intCountLight - 4
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight <= 4):
        GPIO.output(22,GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 2):
        intCountLight = intCountLight - 2
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight >= 2):
        GPIO.output(6, GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 1):
        intCountLight = intCountLight - 1
        GPIO.output(19, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight >= 1):
        GPIO.output(19, GPIO.LOW)
        time.sleep(0.25)
    return render_template('index2.html', **templateData)
@app.route('/startbutton/')
def variable7():
    global intCountDownStart
    intCountDownStart = 1
    while(intCountDownStart == 1):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        global intCount
        intCount = intCount - 1
        intCountLight = intCount
        templateData = {
        'currentCount' : intCountLight
        }
        if(intCountLight >= 16):
            intCountLight = intCountLight - 16
            GPIO.output(4, GPIO.HIGH)
            time.sleep(0.5)
        elif(intCountLight <= 16):
            GPIO.output(4,GPIO.LOW)
            time.sleep(0.25)
        if(intCountLight >= 8):
            intCountLight = intCountLight - 8
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.25)
        elif(intCountLight <= 8):
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.25)
        if(intCountLight >= 4):
            intCountLight = intCountLight - 4
            GPIO.output(22, GPIO.HIGH)
            time.sleep(0.25)
        elif(intCountLight <= 4):
            GPIO.output(22,GPIO.LOW)
            time.sleep(0.25)
        if(intCountLight >= 2):
            intCountLight = intCountLight - 2
            GPIO.output(6, GPIO.HIGH)
            time.sleep(0.25)
        elif(intCountLight >= 2):
            GPIO.output(6, GPIO.LOW)
            time.sleep(0.25)
        if(intCountLight >= 1):
            intCountLight = intCountLight - 1
            GPIO.output(19, GPIO.HIGH)
            time.sleep(0.5)
        elif(intCountLight >= 1):
            GPIO.output(19, GPIO.LOW)
            time.sleep(0.5)
        if(intCount < 1):
            intCountDownStart = 0
            GPIO.output(4, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(19, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(4, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(4,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(6, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(6,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(19, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(19,GPIO.LOW)
            time.sleep(0.1)
    return render_template('index2.html', **templateData)
@app.route('/decreasebutton/')
def variable9():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    global intCount
    intCount = intCount - 1
    intCountLight = intCount
    templateData = {
    'currentCount' : intCountLight
    }
    if(intCountLight >= 16):
        intCountLight = intCountLight - 16
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.5)
    elif(intCountLight <= 16):
            GPIO.output(4,GPIO.LOW)
            time.sleep(0.25)
    if(intCountLight >= 8):
        intCountLight = intCountLight - 8
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight <= 8):
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 4):
        intCountLight = intCountLight - 4
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight <= 4):
        GPIO.output(22,GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 2):
        intCountLight = intCountLight - 2
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.25)
    elif(intCountLight >= 2):
        GPIO.output(6, GPIO.LOW)
        time.sleep(0.25)
    if(intCountLight >= 1):
        intCountLight = intCountLight - 1
        GPIO.output(19, GPIO.HIGH)
        time.sleep(0.5)
    elif(intCountLight >= 1):
        GPIO.output(19, GPIO.LOW)
        time.sleep(0.5)
    if(intCount < 1):
        intCountDownStart = 0
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(4,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(6,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(19, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(19,GPIO.LOW)
        time.sleep(0.1)
    return render_template('index2.html', **templateData)

if __name__=='__main__':
        app.run(debug=True, port=777, host='0.0.0.0')
        GPIO.cleanup()
