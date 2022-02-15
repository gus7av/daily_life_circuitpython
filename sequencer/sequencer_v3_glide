import circuitpython_essentials as cp
import board
import time

gnd_pin = cp.output(board.D1)
btn_pin = cp.input_pullup(board.D4)
tone_pot = cp.analog_input(board.A6)
speed_pot = cp.analog_input(board.A8)
audio_pin = cp.tone_output(board.D7)

gnd_pin.value = False
tones = [196, 220, 247, 262, 294, 330, 370, 392]  # g-major
stored_value = [196] * 16

while True:
    for f in range(16):
        speed = round(cp.map(speed_pot.value, 0, 0xFFFF, 0, 1), 2)
        tone = round(cp.map(tone_pot.value, 0, 0xFFFF, 0, len(tones)-1))
        tone = tones[tone]
        if not btn_pin.value:
            stored_value[f] = tone
        delta = stored_value[f] - stored_value[f-1]
        step = min(1, max(-1, delta))
        if step != 0:
            timer = time.monotonic()
            for i in range(stored_value[f-1], stored_value[f], step):
                audio_pin.value = i
            rest = speed - (time.monotonic() - timer)
            if rest > 0:
                time.sleep(rest)
        else:
            timer = time.monotonic()
            for i in range(0, 0x8000, 512):
                audio_pin.volume = i
            rest = speed - (time.monotonic() - timer) * 2
            if rest > 0:
                time.sleep(rest)
            for i in range(0x8000, 0, -512):
                audio_pin.volume = i
        print(rest)

