#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import build

"""Inspyrator: A program to build scales and chords for most stringed instruments."""

__author__ = "Sal Bruno"
__copyright__ = "Copyright 2017, Sal Bruno"
__license__ = "MIT"
__version__ = "0.01b"
__status__ = "Prototype"



while True:
    user_key = input("In which key would you like to work with?").upper()

    while not build.is_valid_key(user_key, build.chromatic):
        print("I'm sorry, that is not valid input.")
        user_key = input("In which key would you like to work with?").upper()

    if build.is_valid_key(user_key, build.chromatic):
        new_chromatic = build.make_new_chrom(build.chromatic.index(user_key), build.chromatic)
        for step, mode_name in list(enumerate(build.modes)):
            scale_type = build.build_scales(new_chromatic, build.change_mode(step, build.base_mode))
            print(step, mode_name, scale_type)
