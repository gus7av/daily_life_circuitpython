import circuitpython_essentials as cp
import board
import random
import time

led = cp.pwm_output(board.LED)
previous = 128

def split(first, second, offset):

    if offset != 0:
        mid = ((first + second) / 2 + random.randint(-offset, offset))
        offset = int(offset / 2)
        split(first, mid, offset)
        split(mid, second, offset)
    else:
        led.value = int((first * 256)-1)
        time.sleep(0.001)

while True:
    level = random.randint(64, 192)
    split(previous, level, 32)
    previous = level
