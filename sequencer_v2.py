import circuitpython_essentials as cp
import board

tones = 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494
major = 0, 2, 4, 5, 7, 9, 11
minor = 0, 2, 3, 5, 7, 8, 10
fifth = 7
parallel = -3

def circle_of_fifths(scale, step, minor=False):
  if minor:
    return tones[(scale * fifth + parallel + minor[step]) % len(tones)]
  else:
    return tones[(major[step] + scale * fifth) % len(tones)]

key_pot = cp.analog_input(board.A8)
tempo_pot = cp.analog_input(board.A7)
pins = board.A2, board.A3, board.A4, board.A5
step_pots = []
for f in range(len(pins)):
    step_pots.append(cp.analog_input(pins[f]))

while True:   
    for f in range(len(step_pots)):
        tempo = round(cp.map(tempo_pot.value, 0, 0xFFFF, 0, 1), 2)
        key = round(cp.map(key_pot.value, 0, 0xFFFF, 0, (len(tones)-1)))
        step = round(cp.map(step_pots[f].value, 0, 0xFFFF, 0, 7))
        note = circle_of_fifths(key, step) # + knap eller switch til at toggle minor
        cp.play_tone(board.A6, note, tempo)
