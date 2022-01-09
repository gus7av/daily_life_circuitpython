import circuitpython_essentials as cp
import time
import board
from random import randint

led = cp.pwm_output(board.LED)
previous = 128

while True:
    value = randint(64, 247)
    step = min(1, max(-1, value - previous))
    if step != 0:
        for i in range(previous, value, step):
            led.value = (i + randint(-8, 8)) * 255
            time.sleep(0.001)
    previous = value
