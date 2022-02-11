import circuitpython_essentials as cp
import board

f_major = 174, 196, 220, 233, 262, 294, 330, 349
d_minor = 294, 330, 349, 392, 440, 466, 523, 587
c_major = 262, 294, 330, 349, 392, 440, 494, 523
a_minor = 220, 247, 262, 294, 330, 349, 392, 440
g_major = 196, 220, 247, 262, 294, 330, 370, 392
e_minor = 165, 185, 196, 220, 247, 262, 294, 330

keys = f_major, d_minor, c_major, a_minor, g_major, e_minor
key_pot = cp.analog_input(board.A9)
tempo_pot = cp.analog_input(board.A10)
pins = board.A1, board.A2, board.A3, board.A4
step_pots = []
for f in range(len(pins)):
    step_pots.append(cp.analog_input(pins[f]))

while True:
    
    for f in range(len(step_pots)):
        tempo = round(cp.map(tempo_pot.value, 0, 0xFFFF, 0, 1), 2)
        key = round(cp.map(key_pot.value, 0, 0xFFFF, 0, (len(keys)-1)))
        note = round(cp.map(step_pots[f].value, 0, 0xFFFF, 0, 7))
        cp.play_tone(board.A7, keys[key][note], tempo)
