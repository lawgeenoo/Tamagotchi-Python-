from random import randint
import time
import sys


class dog:
    def __init__(self, name, state):
        dog.name = name
        dog.state = ["happy", "sad", "bored", "hungry"]

    def pr(self):
        return '{} is a good dog, take care of her. Iti va zice cand e bai. :) \n f - feed, p -play or pet, q - quit'.format(
            self.name)

    def behaviour():
        b = randint(1, 3)
        if (b == 3):
            jessie.state = dog.state[3]
            return "Jessie is hungry."

        elif (b == 2):
            jessie.state = dog.state[2]
            return "Jessie is bored."

        elif (b == 1):
            jessie.state = dog.state[1]
            return "Jessie is sad."


def menu():
    i = input()
    if (i == '1'):
        pass
    elif (i == '2'):
        sys.exit(0)
    else:
        print("invalid request")
        menu()
        
happiness = 5
jessie = dog("Jessie", 0)
print("1 - Start\n 2 - Quit")
menu()
print(jessie.pr())
while (1):
    rtime = randint(0, 10)
    time.sleep(rtime)
    print(dog.behaviour())
    start = time.time()
    you = input()
    if (you == 'q'):
        sys.exit()
    end = time.time()
    if (int(end - start) >= 30):
        print("You took too long, Jessie felt abandoned and left home.")
        sys.exit(0)
    else:
        pass
    if ((jessie.state == dog.state[3]) and (you == 'f')) or (
        (jessie.state == dog.state[2] or jessie.state == dog.state[1]) and
        (you == 'p')):
        jessie.state = dog.state[0]
        print("Jessie is happy.")
    elif (you == 'q'):
        sys.exit()
    else:
        print("Jessie ain't happy, she wanted something else. ")
        happiness = happiness - 1
    if (happiness == 0):
        print("Jessie got pissed so she ate you.")
        time.sleep(3)
        sys.exit()

    rtime = randint(0, 10)
    time.sleep(rtime)
