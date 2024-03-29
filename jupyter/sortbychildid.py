# -*- coding: utf-8 -*-
"""SortByChildID.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uX3GrfuErlrXlr1AK7EiPvG_W0IspKxC
"""

import pandas as pd

full = pd.read_csv("/content/FullData.csv")
cd = pd.read_csv("/content/ChildDemographic.csv")

ids = cd['TAT'].values # numpy array of TAT ids
for id in ids:
  for valueIndex in range(585):
    if id == full['Subject ID'][valueIndex]:
      # replace the column header
      print(full['Birth date (Child Subject Only)'][valueIndex])