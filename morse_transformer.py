# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 12:14:56 2022

@author: oguztuzun
"""
def morse_transformer(message):
    morse_dictionary = {'a' : '.-', 'b' : '-...', 'c' : '-.-.','d' : '-..','e' : '.','f' : '..-.',
                        'g' : '--.','h' : '....','i' : '..','j' : '.---','k' : '-.-','l' : '.-..',
                        'm' : '--','n' : '-.','o' : '---','p' : '.--.','q' : '--.-','r' : '.-.',
                        's' : '...','t' : '-','u' : '..-','v' : '...-','w' : '.--','x' : '-..-',
                        'y' : '-.--','z' : '--..','1' : '.----','2' : '..---','3' : '...--',
                        '4' : '....-','5' : '.....','6' : '-....','7' : '--...','8' : '---..',
                        '9' : '----.','0' : '-----', ' ' : ' '}
    
    morse_version = ''
    
    for i in message:
        morse_version += morse_dictionary[i.lower()]
        morse_version += ' '
    
    return morse_version[:-1]
