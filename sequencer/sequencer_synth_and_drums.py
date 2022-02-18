import circuitpython_essentials as cp
import board
import time

btn_pin = cp.input_pullup(board.D4)
tone_pot = cp.analog_input(board.A7)
speaker = cp.tone_output(board.D5)

f_major = 174, 196, 220, 233, 262, 294, 330, 349
d_minor = 294, 330, 349, 392, 440, 466, 523, 587
c_major = 262, 294, 330, 349, 392, 440, 494, 523
a_minor = 220, 247, 262, 294, 330, 349, 392, 440
g_major = 196, 220, 247, 262, 294, 330, 370, 392
e_minor = 165, 185, 196, 220, 247, 262, 294, 330

tones = c_major
stored_value = [0] * 16

value = cp.map(tone_pot.value, 0, 0xFFFF, 0.5, 0)
min_duration = 0.1
duration = value + min_duration
sustain = min_duration*0.5 + value*0.1

def glide():
    step = round((tones[stored_value[f]] - tones[stored_value[f-1]])/10)
    if step != 0:
        for i in range(10):
            speaker.value = tones[stored_value[f-1]] + i*step
            time.sleep(sustain/10)
        speaker.value = tones[stored_value[f]]
        time.sleep(duration-sustain)
        speaker.stop()
    else:
        speaker.value = tones[stored_value[f]]
        time.sleep(duration)
        speaker.stop()

def synth():
    speaker.value = tones[stored_value[f]]
    for i in range(0x8000, 0, -0x800):
        speaker.volume = i
        time.sleep(duration/16)
    speaker.stop()

def basic():
    speaker.value = tones[stored_value[f]]
    time.sleep(duration)
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
            time.sleep(duration-sustain)

        # chose tone type for the rest
        else:
            glide()
            # synth()
            # basic()
