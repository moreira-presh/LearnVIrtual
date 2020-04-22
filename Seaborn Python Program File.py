# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:50:15 2020

@author: Precious
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = pd.read_csv('assignment3.txt')
 
data = pd.pivot_table(Data, columns='year', index ='continent', values = 'lifeExp')

 
sns.heatmap(data, cmap ='bone')