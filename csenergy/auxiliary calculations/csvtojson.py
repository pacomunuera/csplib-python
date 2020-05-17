# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:42:52 2020

@author: fmunuera
"""

import csv
import sys
import pandas as pd
#
#with open("sam_sca_physical.csv") as archivocsv:
#    data = csv.DictReader(archivocsv, delimiter=';')
#    output = list()
#    for r in data:
#        output.append(dict(r))
#
#print(json.dump(output, open('sam_sca_physical.json','w'), indent=4, sort_keys=False))


with open("sam_hce_physical.csv") as archivocsv:
    data = pd.read_csv(archivocsv, sep=';', decimal=b'.')

    data.to_json(open('sam_hce_physical.json','w'), orient='records')