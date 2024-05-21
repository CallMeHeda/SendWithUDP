import time
import keyboard

time.sleep(3)
while True:
    keyboard.write('Hello Word!')
    time.sleep(1)
    keyboard.press('enter')
    time.sleep(1)
    keyboard.release('enter')