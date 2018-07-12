# CircuitPython IO demo #1 - General Purpose I/O

import time

import board
from digitalio import DigitalInOut, Direction, Pull



switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:
        print("Waiting")
        time.sleep(0.1)
    else:
        print("FIRE")
        time.sleep(0.1)
