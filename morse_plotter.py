# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:25:05 2022

@author: oguztuzun
"""
from morse_transformer import morse_transformer
import matplotlib.pyplot as plt


def plotter(morse):
    code = []
    code += morse
    signals = []
    units1 = list(range(code.count('.') + code.count('-')*3 + code.count(' ') + len(code)))
    units2use = [i+1 for i in units1]
    for i in code:
        if i == '.':
            signals.append(1)
            signals.append(0)
        elif i == '-':
            for i in range(3):
                signals.append(1)
            signals.append(0)
        elif i == ' ':
            for i in range(2):
                signals.append(0)

    plt.plot(units2use, signals)
            
    plt.show()
    return code
  


