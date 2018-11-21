#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:22:10 2018

@author: ericpeter
"""

import locale


class ReportGenerator:
    creator = 'Me Myself and I'
    diplo=2012

    @property
    def lang(self):
        loc, enc= locale.getlocale()
        return loc[:2]

        
    def greeting(self):
        if self.lang == 'en':
            print('Hello')
        elif self.lang =='fr':
            print('bonjour')
            
    def goodbye(self):
        if self.lang =='en':
            print('See you')
        elif self.lang=='fr':
            print('A+')
        

reportg=ReportGenerator()

reportg.lang

reportg.greeting()
