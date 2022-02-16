import circuitpython_essentials as cp
import board
import time
import random

gnd_pin = cp.output(board.D1)
btn_pin = cp.input_pullup(board.D4)
tone_pot = cp.analog_input(board.A6)
speed_pot = cp.analog_input(board.A8)
speaker = cp.tone_output(board.D7)

gnd_pin.value = False
tones = [196, 220, 247, 262, 294, 330, 370, 392]  # g-major
stored_value = [0] * 16

while True:
    for f in range(16):
        speed = round(cp.map(speed_pot.value, 0, 0xFFFF, 0.1, 1), 2)
        tone = round(cp.map(tone_pot.value, 0, 0xFFFF, 0, len(tones)-1))
        
        # record button
        if not btn_pin.value:
            stored_value[f] = tone
        
        # bass-drum
        if stored_value[f] == 0:
            timer = time.monotonic()
            for i in range(196, 98, -2):
                speaker.value = i
                time.sleep(0.001)
            speaker.stop()
            duration = time.monotonic() - timer
            time.sleep(speed-duration)
        
        # snare-drum
        elif stored_value[f] == 7:
            timer = time.monotonic()
            for i in range(1, 40):
                speaker.value = 392 + random.randrange(-i, i)
                time.sleep(0.001)
            speaker.stop()
            duration = time.monotonic() - timer
            time.sleep(speed - duration)
        
        # tone
        else:
            speaker.value = tones[stored_value[f]]
            time.sleep(speed)
            speaker.stop()
