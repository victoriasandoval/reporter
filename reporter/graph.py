#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:47:12 2018

@author: ericpeter
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from pathlib import Path

module_dir = os.path.abspath(os.path.dirname(__file__))

print(module_dir)

def graph(file=Path(module_dir)/'../data/series-1800-2015_simplified.xlsx'
          ,output_file=Path(module_dir)/'../data/graph.png'):


    
    
    data=pd.read_excel(file)
    datat = data.T
    serie = datat.loc['Série']
    datat = datat.drop(['Série'])
    datat.index = datat.index.astype(int)
    
    ax=datat.plot(y=19,label=serie.loc[19])
    
    ax=datat.plot(y=34,ax=ax,label=serie.loc[34])

    graph=datat.plot(y=36,ax=ax,label=serie.loc[36],secondary_y=True)
    
    graph.figure.savefig(output_file)
    
    
    