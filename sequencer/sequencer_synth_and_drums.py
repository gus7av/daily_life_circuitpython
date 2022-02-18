import circuitpython_essentials as cp
import board
import time

btn_pin = cp.input_pullup(board.D4)
tone_pot = cp.analog_input(board.A7)
speaker = cp.tone_output(board.D5)

tones = [196, 220, 247, 262, 294, 330, 370, 392]  # g-major
stored_value = [0] * 16

value = cp.map(tone_pot.value, 0, 0xFFFF, 0.5, 0)
min_speed = 0.1
speed = value + min_speed
sustain = min_speed*0.5 + value*0.1

def glide():
    step = round((tones[stored_value[f]] - tones[stored_value[f-1]])/10)
    if step != 0:
        for i in range(10):
            speaker.value = tones[stored_value[f-1]] + i*step
            time.sleep(sustain/10)
        time.sleep(speed-sustain)
        speaker.stop()
    else:
        speaker.value = tones[stored_value[f]]
        time.sleep(speed)
        speaker.stop()
 
def synth(): 
    speaker.value = tones[stored_value[f]]
    for i in range(0x8000, 0, -0x800):
        speaker.volume = i
        time.sleep(speed/16)
    speaker.stop()
    
def basic():
    speaker.value = tones[stored_value[f]]
    time.sleep(speed)
    speaker.stop()

while True:
    for f in range(16):
        tone = round(cp.map(tone_pot.value, 0, 0xFFFF, 0, len(tones)-1))

        # record button
        if not btn_pin.value:
            stored_value[f] = tone

        # percussion tones on 0 and 7
        if stored_value[f] == 0 or stored_value[f] == 7:
            for i in range(tones[stored_value[f]], tones[stored_value[f]]-100, -10):
                speaker.value = i
                time.sleep(sustain/10)
            speaker.stop()
            time.sleep(speed-sustain)

        # chose tone type for the rest
        else:
            glide()
            # synth()
            # basic()
