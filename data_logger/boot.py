import circuitpython_essentials as cp
import board
import storage

switch = cp.DigitalIn(board.D4)
switch.pull_up()
storage.remount("/", switch.value)
