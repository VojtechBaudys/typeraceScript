import keyboard
from time import time as currentTime
from functions import getInput, log, stats

run = True
speed = 0.00000001

while(run):
    text = getInput('Text: ')
    startT = currentTime()

    for letter in text:
        keyboard.write(letter, speed)
        log(startT, letter)

    if(stats(startT, text) == 'exit'):
        break
    