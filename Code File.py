# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:33:17 2020

@author: Precious
"""

#Importing Library
import pandas as pd

#
#To read up the (excel) file using pandas
Excelfile = 'Input_File.xlsx'
all_sheets = pd.read_excel(Excelfile, sheet_name = None)

#Exporting each excel sheet to csv files 
sheets = all_sheets.keys()
for sheet_name in sheets:
    sheet = pd.read_excel(Excelfile, sheet_name =sheet_name)
    sheet.to_csv('%s.csv' %sheet_name, index = False)