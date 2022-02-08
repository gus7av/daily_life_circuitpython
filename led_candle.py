import circuitpython_essentials as cp
import time
import board
from random import randint

led = cp.pwm_output(board.LED)
previous = 0x8000
flicker = 0x2000

while True:
    value = randint(flicker, 0xFFFF - flicker)
    step = min(256, max(-256, value - previous))
    if step != 0:
        for i in range(previous, value, step):
            led.value = i + randint(-flicker, flicker)
            time.sleep(0.001)
    previous = value
