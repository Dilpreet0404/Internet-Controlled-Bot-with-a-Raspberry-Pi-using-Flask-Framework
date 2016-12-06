import time
from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
pin1 = 29
pin2 = 31
pin3 = 33
pin4 = 37
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

@app.route("/")
@app.route("/<state>")
def Bot_move(state=None):
    if state == 'Forward':
    	GPIO.output(pin1,GPIO.HIGH)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.HIGH)                                          
        GPIO.output(pin4,GPIO.LOW)
	time.sleep(1)
     	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.LOW)
    if state == 'Back':
    	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.HIGH)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.HIGH)
	time.sleep(1)
     	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.LOW)    	
    if state == 'Right':
    	GPIO.output(pin1,GPIO.HIGH)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.HIGH)
	time.sleep(1)
     	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.LOW)    	
    if state == 'Left':
    	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.HIGH)
	GPIO.output(pin3,GPIO.HIGH)                                          
        GPIO.output(pin4,GPIO.LOW)
	time.sleep(1)
     	GPIO.output(pin1,GPIO.LOW)                                          
        GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)                                          
        GPIO.output(pin4,GPIO.LOW)    	
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
                

