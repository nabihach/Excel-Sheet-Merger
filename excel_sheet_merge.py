import pandas as pd
import numpy as np
import os, collections, csv
from os.path import basename

# This script concatenates the sheets (named 'Table 1', 'Table 2', ... so on) of an Excel file into a single sheet. 
df = []
f = "/home/.../file3.xlsx" #Modify this. This is the path to the Excel file  
numberOfSheets = 477 #Modify this. 

for i in range(1,numberOfSheets+1):
    data = pd.read_excel(f, sheetname = 'Table '+str(i), header=None) #Modify the sheetname argument based on how your sheets are named
    df.append(data)
final = "/home/.../mergedfile3.xlsx" #Path to the file in which new sheet will be saved.
df = pd.concat(df)
df.to_excel(final)
