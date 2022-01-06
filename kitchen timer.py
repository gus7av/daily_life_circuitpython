import circuitpython_essentials as cp
import time
import board
import alarm

btn = cp.input_pullup(board.IO0)
time_out = 2  # seconds
debounce = 0.1

timer = time.monotonic()
previous = False
count = 1

def start_timer():
    cp.play_tone(board.IO3, 500, 0.1)
    cp.play_tone(board.IO3, 1000, 0.1)
    btn.disable()
    sec = count * 1
    time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + sec)
    pin_alarm = alarm.pin.PinAlarm(pin=board.IO0, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)

def power_down():
    cp.play_tone(board.IO3, 1000, 0.1)
    cp.play_tone(board.IO3, 500, 0.1)
    while not btn.value:
        time.sleep(0.1)
    btn.disable()
    pin_alarm = alarm.pin.PinAlarm(pin=board.IO0, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

if isinstance(alarm.wake_alarm, alarm.time.TimeAlarm):
    while btn.value:
        cp.play_tone(board.IO3, 1000, 0.1)
        time.sleep(0.1)
    while not btn.value:
        time.sleep(0.1)
    power_down()

if not alarm.wake_alarm:
    power_down()

cp.play_tone(board.IO3, 1000, 0.1)
print(count)

while True:
    if time.monotonic() - timer > time_out and btn.value:
        start_timer()

    if time.monotonic() - timer > time_out and not btn.value:
        power_down()

    value = btn.value
    if value != previous:
        if not value and time.monotonic() - timer > debounce:
            count += 1
            cp.play_tone(board.IO3, 1000, 0.1)
            print(count)
        timer = time.monotonic()
    previous = value
