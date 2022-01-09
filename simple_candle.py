import circuitpython_essentials as cp
import time
from random import randint
import board

led = cp.output(board.LED)
value = 32767

while True:
    value += randint(max(-4, -value), min(4, 65535 - value))
    led.value = value
    time.sleep(0.001)
