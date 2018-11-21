#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:33:37 2018

@author: ericpeter
"""

from requests_html import HTMLSession 
from random import randint

randint(0,len(poems))


session = HTMLSession()
r = session.get("https://fr.wikisource.org/wiki/Po%C3%A9sies_(Rimbaud)/%C3%A9d._Vanier,_1895/Le_Bateau_ivre")
poems = [poem.text for poem in r.html.find("div.poem")]




poems[0].split('\n')[0]



print(poems)