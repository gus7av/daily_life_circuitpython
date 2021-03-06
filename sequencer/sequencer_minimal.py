import circuitpython_essentials as cp
import board

gnd_pin = cp.output(board.D1)
btn_pin = cp.input_pullup(board.D4)
tone_pot = cp.analog_input(board.A6)
speed_pot = cp.analog_input(board.A8)

gnd_pin.value = False
tones = [196, 220, 247, 262, 294, 330, 370, 392]  # g-major
stored_value = [0] * 16

while True:
    for f in range(16):
        speed = round(cp.map(speed_pot.value, 0, 0xFFFF, 0, 1), 2)
        tone = round(cp.map(tone_pot.value, 0, 0xFFFF, 0, len(tones)-1))
        if not btn_pin.value:
            stored_value[f] = tone
        cp.play_tone(board.D7, tones[stored_value[f]], speed)
