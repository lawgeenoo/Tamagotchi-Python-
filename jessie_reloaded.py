import threading
import time
import sys
from random import randint

#--------------- CLASSES & METHODS---------------------------#
class dog():
    def __init__(self, name, state):
        dog.name = name
        dog.state = ["happy", "sad", "bored", "hungry", "abandoned", "disturbed"]    # init dog name and attributes

    def pr(self):
        return '{} is a good dog, take care of her. Iti va zice cand e bai. :) \n f - feed, p -play or pet, q - quit'.format(
            self.name)                                                              #intro

    def behaviour():                                                                #dog's random behaviour method
        global happiness
        if happiness == 0:
            return
        b = randint(1, 3)
        if (b == 4):
          jessie.state = dog.state[4]
          return "Jessie felt abandoned and left home."
        elif (b == 3):
            jessie.state = dog.state[3]
            return "Jessie is hungry."

        elif (b == 2):
            jessie.state = dog.state[2]
            return "Jessie is bored."

        elif (b == 1):
            jessie.state = dog.state[1]
            return "Jessie is sad."
      


#------------------------------GLOBAL VARS--------------------------------------------#
p = None    #input variable 
chron = 0   #the chronometer/timer variable
happiness = 5   #happiness variable, once to 0 dog leaves.
jessie = dog("Jessie", 0) #intialization of the dog "object"
highscore = 0               #your final score

print(jessie.pr())     

def timer():                                                                    # threaded timer, dog will leave if left unnatended
    global chron
    while chron <=10:    
      chron = chron + 1
      time.sleep(1)
    print(dog.name, "got upset and left.")
    print("HiScore: ", highscore)
    chron = 11
    time.sleep(1)
    sys.exit(0)

def checkinput():                                                               # your interaction with the dog - evaluation of your actions
    while True:
        global p, rtime, happiness, chron, highscore
        rtime = randint(3, 5)
        p = input()
        if chron < rtime -1: 
            print("You disturbed Jessie.")
            happiness = happiness - 1
            chron = 0
            rtime = randint(3,5)
            if happiness == 0:
                chron = 11
                break
            
        elif jessie.state == dog.state[3] and p == 'f' or jessie.state == dog.state[2] and p == 'p' or jessie.state == dog.state[1] and p == 'p':
             jessie.state == dog.state[0]
             print("Jessie is happy.")
             highscore = highscore + 1
        else:
            print("That's not what Jessie wanted.")
            happiness = happiness + 1
        chron = 0
        if p == 'q' or happiness == 0 :
            chron = 11   # thread kill hardcode
            return

def bhv():    # displaying dog behaiour
    global rtime, chron
    while True: 
            time.sleep(rtime)
            print(dog.behaviour())
            rtime = randint(3, 5)
            if chron == 11:
                break
#----------------------------------THREADS----------------------#
t = threading.Thread(target = timer)
c = threading.Thread(target = checkinput)
b = threading.Thread(target = bhv)
t.start()
c.start()
b.start()


