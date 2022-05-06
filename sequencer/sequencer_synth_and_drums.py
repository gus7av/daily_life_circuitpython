import circuitpython_essentials as cp
import board
import time

rec_pin = cp.DigitalIn(board.D6)
rec_pin.pull_up()

del_pin = cp.DigitalIn(board.D0)
del_pin.pull_up()

btn_gnd = cp.DigitalOut(board.D4)
btn_gnd.value = False

tone_pot = cp.AnalogIn(board.D3)

pot_pwr = cp.DigitalOut(board.D5)
pot_pwr.value = True

speaker = cp.ToneOut(board.D8)

f_major = 174, 196, 220, 233, 262, 294, 330, 349
d_minor = 294, 330, 349, 392, 440, 466, 523, 587
c_major = 262, 294, 330, 349, 392, 440, 494, 523
a_minor = 220, 247, 262, 294, 330, 349, 392, 440
g_major = 196, 220, 247, 262, 294, 330, 370, 392
e_minor = 165, 185, 196, 220, 247, 262, 294, 330
scale = c_major
previous_note = scale[0]

steps = 32
bars = int(steps / 4)
bar = [0, 8, 0, 8]
stored_value = bar * bars

value = cp.map_range(tone_pot.value, 0, 0xFFFF, 0.5, 0)
min_duration = 0.1
duration = value + min_duration
sustain = min_duration * 0.5 + value * 0.1

while True:
    for f in range(steps):

        # delete button
        if not del_pin.value:
            stored_value[f] = 8

        # record button
        if not rec_pin.value:
            stored_value[f] = round(
                cp.map_range(tone_pot.value, 0, 0xFFFF, 0, len(scale) - 1)
            )

        # percussion tones on 0 and 7
        if stored_value[f] == 0 or stored_value[f] == 7:
            for i in range(
                scale[stored_value[f]],
                int(scale[stored_value[f]] / 2),
                -int(scale[stored_value[f]] / 20),
            ):
                speaker.value = i
                time.sleep(sustain / 10)
            speaker.stop()
            time.sleep(duration - sustain)

        # silence on 8
        elif stored_value[f] == 8:
            speaker.stop()
            time.sleep(duration)

        # glide from previous tone on the rest
        else:
            note = scale[stored_value[f]]
            step = round((note - previous_note) / 10)
            if step != 0:
                for i in range(10):
                    speaker.value = previous_note + i * step
                    time.sleep(sustain / 10)
                speaker.value = scale[stored_value[f]]
                time.sleep(duration - sustain)
                speaker.stop()
            else:
                speaker.value = scale[stored_value[f]]
                time.sleep(duration)
                speaker.stop()
            previous_note = scale[stored_value[f]]
