"""Inspyrator: A program to build scales and chords for most stringed instruments."""

__author__ = "Sal Bruno"
__copyright__ = "Copyright 2017, Sal Bruno"
__license__ = "MIT"
__version__ = "0.01b"
__status__ = "Prototype"


chromatic = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# Base scale mode
base_mode = [2, 2, 1, 2, 2, 2, 1]  # The "Major" scale.

# Seven modes of the Major scale.
modes = [
    'ionian (Major)',
    'dorian',
    'phrygian',
    'lydian',
    'mixolydian',
    'aeolian (minor)',
    'locrian'
    ]

def is_valid_key(user_key_input, chrom):
    """
    Checks for valid user input.
    """

    if len(user_key_input) != 1 and len(user_key_input) != 2:
        return False
    elif user_key_input not in chrom:
        return False
    else:
        return user_key_input


def make_new_chrom(scale_key, chrom):
    """
    Rearranges the notes to start on given element.
    """

    new_chrom = chrom[scale_key:] + chrom[:scale_key]
    new_chrom.append(chrom[scale_key])  # Append first note to end of list.

    return new_chrom


def change_mode(mode, base):
    """
    Changes the modes.
    """

    new_mode = base[mode:] + base[:mode]
    return new_mode


def build_scales(new_chrom, base):
    """
    Builds the major scale from new chromatic.
    """

    scale_step = 0
    major_scale = [new_chrom[scale_step]]
    for step in base:
        scale_step += step
        major_scale.append(new_chrom[scale_step])
    return major_scale


while True:
    user_key = input("In which key would you like to work with?").upper()

    while not is_valid_key(user_key, chromatic):
        print("I'm sorry, that is not valid input.")
        user_key = input("In which key would you like to work with?").upper()

    if is_valid_key(user_key, chromatic):
        new_chromatic = make_new_chrom(chromatic.index(user_key), chromatic)
        for step, mode_name in list(enumerate(modes)):
            scale_type = build_scales(new_chromatic, change_mode(step, base_mode))
            print(step, mode_name, scale_type)
