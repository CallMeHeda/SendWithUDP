import time
import keyboard
import random

def write(phrase):
    keyboard.write('Hello Word!')
    time.sleep(1)
    keyboard.press('enter')
    time.sleep(1)
    keyboard.release('enter')

def random_keys():
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
            'enter', 'space', 'backspace', 'tab', 'esc', 'up', 'down', 'left', 'right']
    
    random_key = random.choice(keys)
    time.sleep(1)
    keyboard.press(random_key)
    time.sleep(1)
    keyboard.release(random_key)

# time.sleep(3)
# while True:
    # write('Hello Word!')
    # keyboard.write('Hello Word!')
    # time.sleep(1)
    # keyboard.press('enter')
    # time.sleep(1)
    # keyboard.release('enter')
    
random_keys()