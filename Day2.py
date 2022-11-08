# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:51:29 2022

@author: Jordan Turley
"""

#%% Imports
import pandas as pd

#%% Read in data
data = pd.read_csv(r'C:\Users\Jordan Turley\Documents\GitHub\AdventOfCode2020\Inputs\2.txt', header = None)
data.columns = ['input']

#%% Part 1
#Get min/max/letter/password
data = data['input'].str.split('-| ',expand=True)
data.columns = ['min','max','letter','password']
data['letter'] = data['letter'].str[:1]
data['min'] = data['min'].astype(int)
data['max'] = data['max'].astype(int)
#Get letter count
data['count'] = data.apply(lambda x: x.password.count(x.letter), axis=1)
#check
data['valid'] = (data['count']>=data['min'])&(data['count']<=data['max'])

print(data['valid'].sum())

#%% Part 2
data['letter1'] = data.apply(lambda x: x.password[x['min']-1], axis=1)
data['letter2'] = data.apply(lambda x: x.password[x['max']-1], axis=1)

#check
data['valid'] = ((data['letter1']==data['letter'])|(data['letter2']==data['letter']))&(data['letter2']!=data['letter1'])
print(data['valid'].sum())
