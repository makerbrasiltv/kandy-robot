#!/usr/bin/python

import RPi.GPIO as G
import time
import os

G.setmode(G.BOARD)

TRIG = 18
ECHO = 23
#print "Medindo distancia em processo"
G.setup(TRIG,G.OUT)
G.output(TRIG,0)	
G.setup(ECHO, G.IN)
time.sleep(0.1)
G.output(TRIG,1)
time.sleep(0.00001)
G.output(TRIG,0)

while G.input(ECHO) == 0:
  pass
start = time.time()

while G.input(ECHO) == 1:
  pass
stop = time.time()

valor = (stop - start) * 17000

souInt = int(valor)
souStr = str(souInt)

os.system("espeak -v pt+f4 " +souStr)

time.sleep(0.1)

os.system("espeak -v pt+f4 -s 120 'centimetros'")

#t = datetime.now()stltime("%k %M")

G.cleanup()

time.sleep(3)
