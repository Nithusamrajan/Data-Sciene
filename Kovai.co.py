from itertools import dropwhile
from traceback import print_tb
from unittest.mock import inplace

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from contourpy.array import remove_nan
from debugpy.launcher.debuggee import describe
from numpy.lib.recfunctions import drop_fields
from pandas.io.pytables import dropna_doc

#preparing the dataframe
d = pd.read_csv('Daily_Public_Transport_Passenger_Journeys_by_Service_Type_20241128.csv',sep=",")
df = pd.DataFrame(data=d)
print(df)

#Removing the null values in table
d.dropna(axis=0,inplace=True)
print(d)

#Identifying data types
print(d.info())

#creating a summary of the data
print(d.describe())

