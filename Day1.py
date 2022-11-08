# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:41:44 2022

@author: Jordan Turley
"""
#%% Imports
import pandas as pd

#%% Read in data
data = pd.read_csv(r'C:\Users\Jordan Turley\Documents\GitHub\AdventOfCode2020\Inputs\1.txt', header = None)

#%% Part 1
#Crossjoin them
data['temp'] = 1
matched = pd.merge(data,data, on = 'temp')
matched['sum'] = matched['0_x'] + matched['0_y']
matched = matched[matched['sum'] == 2020].iloc[0]
output = matched['0_x']*matched['0_y']
print(output)

#%% Part 2
#Multiple by data again
matched = pd.merge(data,data, on = 'temp')
matched = pd.merge(matched,data, on = 'temp')
matched['sum'] = matched['0_x'] + matched['0_y'] +  matched[0]
matched = matched[matched['sum'] == 2020].iloc[0]
output = matched['0_x']*matched['0_y']*matched[0]
print(output)
