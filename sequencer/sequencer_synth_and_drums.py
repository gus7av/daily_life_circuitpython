import circuitpython_essentials as cp
import board
import time

btn_pin = cp.DigtitalIn(board.D4)
btn_pin.pull_up()

tone_pot = cp.AnalogIn(board.A7)
speaker = cp.ToneOut(board.D5)

f_major = 174, 196, 220, 233, 262, 294, 330, 349
d_minor = 294, 330, 349, 392, 440, 466, 523, 587
c_major = 262, 294, 330, 349, 392, 440, 494, 523
a_minor = 220, 247, 262, 294, 330, 349, 392, 440
g_major = 196, 220, 247, 262, 294, 330, 370, 392
e_minor = 165, 185, 196, 220, 247, 262, 294, 330
scale = c_major

steps = 32
stored_value = [0] * steps

value = cp.map_range(tone_pot.value, 0, 0xFFFF, 0.5, 0)
min_duration = 0.1
duration = value + min_duration
sustain = min_duration * 0.5 + value * 0.1


def glide():
    step = round((scale[stored_value[f]] - scale[stored_value[f - 1]]) / 10)
    if step != 0:
        for i in range(10):
            speaker.value = scale[stored_value[f - 1]] + i * step
            time.sleep(sustain / 10)
        speaker.value = scale[stored_value[f]]
        time.sleep(duration - sustain)
        speaker.stop()
    else:
        speaker.value = scale[stored_value[f]]
        time.sleep(duration)
        speaker.stop()


def synth():
    speaker.value = scale[stored_value[f]]
    for i in range(0x8000, 0, -0x800):
        speaker.volume = i
        time.sleep(duration / 16)
    speaker.stop()


def basic():
    speaker.value = scale[stored_value[f]]
    time.sleep(duration)
    speaker.stop()


while True:
    for f in range(steps):
        tone = round(cp.map_range(tone_pot.value, 0, 0xFFFF, 0, len(scale) - 1))

        # record button
        if not btn_pin.value:
            stored_value[f] = tone
        # percussion tones on 0 and 7
        if stored_value[f] == 0 or stored_value[f] == 7:
            step = round(scale[stored_value[f]] / -20)
            for i in range(10):
                speaker.value = scale[stored_value[f]] + i * step
                time.sleep(sustain / 10)
            speaker.stop()
            time.sleep(duration - sustain)
        # chose tone type for the rest
        else:
            glide()
            # synth()
            # basic()
