# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:42:52 2020

@author: fmunuera
"""

import csv
import sys
import os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
from datetime import datetime, timedelta
import time
import pandas as pd
import plotly.express as px


filename_sam = 'simulations_outputs/results dow A.csv'
filename_simulation = 'simulations_outputs/20200614 173626 TEST 2007 IPH DOWA_COMPLETE.csv'
filename_columns = 'simulations_outputs/c.csv'

with open(filename_simulation) as file_simulation:
    data_simulation = pd.read_csv(
        file_simulation,
        sep=';',
        decimal=b',',
        index_col=0,
        parse_dates=[0])

with open(filename_sam) as file_sam:
    data_sam = pd.read_csv(
        file_sam,
        sep=',',
        decimal=b'.',
        # dayfirst=True,
        index_col=0,
        parse_dates=[0],
        date_parser= lambda x: datetime.strptime(x, "%b %d, %I:%M %p"))

with open(filename_columns) as file_columns:
    columns_df = pd.read_csv(
        file_columns,
        sep=';',
        encoding="cp1252")

simulation_year = data_simulation.index[0].year

data_sam.index = data_sam.index.map(
    lambda t: t.replace(year=simulation_year))

d = timedelta(hours=1)

data_sam.index = data_sam.index - d

result = data_simulation.join(data_sam, how='left')

result['Field total mass flow | (kg/s)'] = (
    result['Field total mass flow delivered | (kg/s)'] +
    result['Field total mass flow recirculated | (kg/s)'])

for c in columns_df.columns:
    if c not in result.columns:
        result[c]=''

result = result.reindex(columns=columns_df.columns)


prefix = datetime.today().strftime("%Y%m%d %H%M%S ")
result.to_csv(
    'simulations_outputs/'+prefix+'COMBINADO IPH.csv', sep=';', decimal=',',
    encoding="cp1252")



