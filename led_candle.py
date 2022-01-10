import circuitpython_essentials as cp
import time
import board
from random import randint

led = cp.pwm_output(board.LED)
previous = 32767
flicker = 8191

while True:
    value = randint(flicker, 65535 - flicker)
    step = min(255, max(-255, value - previous))
    if step != 0:
        for i in range(previous, value, step):
            led.value = i + randint(-flicker, flicker)
            time.sleep(0.001)
    previous = value
