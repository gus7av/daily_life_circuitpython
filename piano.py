import circuitpython_essentials as cp
import board

f_major = 174, 196, 220, 233, 262, 294, 330, 349
d_minor = 294, 330, 349, 392, 440, 466, 523, 587
c_major = 262, 294, 330, 349, 392, 440, 494, 523
a_minor = 220, 247, 262, 294, 330, 349, 392, 440
g_major = 196, 220, 247, 262, 294, 330, 370, 392
e_minor = 165, 185, 196, 220, 247, 262, 294, 330

scales = f_major, d_minor, c_major, a_minor, g_major, e_minor
current_scale = 2

next_scale = cp.input_pullup(board.D9)
prev_scale = cp.input_pullup(board.D10)
previous = next_scale.value
previous_2 = prev_scale.value

pins = board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8
keys = []
for f in range(len(pins)):
    keys.append(cp.input_pullup(pins[f]))

while True:
    for f in range(8):
        if not keys[f].value:
            cp.play_tone(board.A0, scales[current_scale][f], 0.1)

    value = next_scale.value
    if not value and previous:
        current_scale += 1
        current_scale = min(current_scale, (len(scales)-1))
    previous = value

    value_2 = prev_scale.value
    if not value_2 and previous_2:
        current_scale -= 1
        current_scale = max(current_scale, 0)
    previous_2 = value_2
