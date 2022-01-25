import circuitpython_essentials as cp
import board
import storage

switch = cp.input_pullup(board.D4)
storage.remount("/", switch.value)
