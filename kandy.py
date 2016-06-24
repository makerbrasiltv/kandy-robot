#!/usr/bin/python

import RPi.GPIO as G
import time
import os

person = "alguem no alem"
souInt = 0

def neural(person, souInt):
   
   sensorUS()   
   
   if souInt <= 50:
      while True:   
         print "Ola, meu nome e Kandy."
         time.sleep(5)
         print "Quem nao gosta de chocolates, nao e ?"
         time.sleep(3)
         print "Por favor, aceite estes chocolates"
         
         #####
         ##### Despeja chocolates
         #####
	 print "#### Chocolates na bandeja ####"

         if souInt <= 50:
            while souInt > 50:
               print "aguardando a saida"
            print "Saindo do loop"
            time.sleep(3)

   elif souInt <= 20:
      print 'Eu sou 20'
      talk = "ola 20 "
   else:
      print "Ola, "+person
      talk = "..."
   
   lastTalk = talk


def sensorUS():

   ##############################
   #+++++++ start sensor +++++++#
   ##############################

   G.setmode(G.BOARD)
   TRIG = 18
   ECHO = 23
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

   # ver como implementar a ultima fala e passar para a funcao
  
   # neural(person, souInt)

   ##### os.system("espeak -v pt+f4 " +souStr)

   # time.sleep(0.1)

   ##### os.system("espeak -v pt+f4 -s 120 'centimetros'")

   #t = datetime.now()stltime("%k %M")

   print souInt
   print "-------------------------------------------"

   return souInt

   G.cleanup()


neural(person, souInt)
