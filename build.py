#  12 toners kromatic skala.
chromatic = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# Base scale mode
base_mode = [2, 2, 1, 2, 2, 2, 1]  # "Dur" Skala.

# Seven modes of the Major scale.
modes = [
    'ionisk (Dur)',
    'dorisk',
    'phrygisk',
    'lydisk',
    'mixolydisk',
    'aeolisk (mol)',
    'locrisk'
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
    Laver dur skala from new chromatic.
    """

    skala_step = 0
    dur_skala = [new_chrom[skala_step]]
    for step in base:
        skala_step += step
        dur_skala.append(new_chrom[skala_step])
    return dur_skala
