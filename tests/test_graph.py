#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:58:05 2018

@author: ericpeter
"""

import os
import tempfile
from reporter.graph import graph

def test_graph():
    
    fichier=tempfile.mktemp("graph.png")
    
    graph(file='/Users/ericpeter/Documents/reporter/data/series-1800-2015_simplified.xlsx'
          ,output_file=fichier)
    
    
    assert os.path.isfile(fichier)
    
    