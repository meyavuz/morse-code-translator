# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 15:53:09 2022

@author: oguztuzun
"""

from morse_transformer import morse_transformer
from morse_plotter import plotter
from sound_player import sound_player

message = input('Enter your message: ')

plotter(morse_transformer(message))  

sound_player(morse_transformer(message))