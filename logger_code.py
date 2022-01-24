import circuitpython_essentials as cp
import time
import board

led = cp.output(board.LED)

try:
    with open("/temperature.txt", "a") as fp:
        temp = cp.temperature()
        fp.write('{0:.2f}\n'.format(temp))
        fp.flush()
        cp.deep_sleep(600)
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        led.value = not led.value
        time.sleep(delay)
