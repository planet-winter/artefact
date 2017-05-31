#!/usr/bin/python

#import RPi.GPIO as GPIO
import json
import urllib


##GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.IN)
#GPIO.setup(12, GPIO.OUT)



def marrysay(phrase):

    url = 'http://pegasus.noise:5000/'
    values = {'text': phrase,
              'submit': 'SUBMIT'}

    html = urllib.urlopen(url, urllib.urlencode(values)).read()
    #print html


    
marrysay("I am a peace of art, leave me alone")

#while True:
#
#      if not GPIO.input(11):
#              GPIO.output(12, True)
#      else:
#              GPIO.output(12, False)
#              GPIO.cleanup()
