import circuitpython_essentials as cp
import board
# import time

keys = []
c_scale = 262, 294, 330, 349, 392, 440, 494, 523
pins = board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8
for f in range(len(pins)):
    keys.append(cp.input_pullup(pins[f]))

while True:
    for f in range(8):
        if not keys[f].value:
            cp.play_tone(board.AO, c_scale[f])
