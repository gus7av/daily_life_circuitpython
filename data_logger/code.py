import circuitpython_essentials as cp
import time
import board

led = cp.DigitalOut(board.LED)

try:
    with open("/temperature.txt", "a") as fp:
        temp = cp.temperature()
        time_passed = time.monotonic()
        hours = int(time_passed / 3600)
        minutes = int((time_passed % 3600) / 60)
        seconds = int(time_passed % 60)        
        fp.write('{0:02}:{1:02}:{2:02},{3:.2f}\n'.format(hours, minutes, seconds, temp))
        fp.flush()
        cp.deep_sleep(10)
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        led.value = not led.value
        time.sleep(delay)
