# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:22:39 2022

@author: oguztuzun
"""

import winsound
def sound_player(liste):
    for i in liste:
        if i == '-':
            winsound.PlaySound('morse_sound_long', winsound.SND_FILENAME)
        elif i == '.':
            winsound.PlaySound('morse_sound_short', winsound.SND_FILENAME)
        elif i == ' ':
            winsound.PlaySound('morse_sound_blank', winsound.SND_FILENAME)