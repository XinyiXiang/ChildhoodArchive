import numpy as np
import pandas as pd
import os


os.listdir()

table = pd.read_excel("ChildObservation_MasterFile.xlsx")


table.head()


target_rows = [table[table.TargetPerson.astype(str)=='7']
              , table[table.present1.astype(str)=='7'],
              table[table.present2.astype(str)=='7'],table[table.present3.astype(str)=='7'],
              table[table.present4.astype(str)=='7'],table[table.present5.astype(str)=='7'],
              table[table.present6.astype(str)=='7'],table[table.present7.astype(str)=='7'],
              table[table.present8.astype(str)=='7'],table[table.present9.astype(str)=='7'],
              table[table.present10.astype(str)=='7'],table[table.present11.astype(str)=='7'],
              table[table.present12.astype(str)=='7']
               ]
df_7 = pd.concat(target_rows)



df_7.head()
