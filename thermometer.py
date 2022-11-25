import board
import time
import digitalio
import microcontroller

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

while True:
    temperature = round(microcontroller.cpu.temperature)
    print(temperature)
    for i in range(5):
        if temperature % 2 ** (i + 1) >= 2 ** i:
            led.value = True
            time.sleep(0.5)
            led.value = False
            time.sleep(0.5)
        else:
            led.value = True
            time.sleep(0.1)
            led.value = False
            time.sleep(0.9)
    time.sleep(2)
