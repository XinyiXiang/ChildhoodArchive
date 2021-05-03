import xlrd
import pandas as pd
from re import search

# read file
df = pd.read_excel('sheet.xlsx')

location = ("/content/test.xlsx")
wb = xlrd.open_workbook(location)
sheet = wb.sheet_by_index(0)

#for col in df.columns.values.tolist():
for row in range(sheet.nrows):
  # subtract one to avoid single index exceeding bounds since xlsx is 0-indexed
  cell_texts = df.iloc[row-1]['Picture1']
  count = 0
  for line in cell_texts.split('\n'):
    if "····" in line or "……" in line or "..." in line or "···" in line:
      count+=1
    p_num = str(df.iloc[row-1]['P#'])
  print("Picture 1 - " + p_num + ":" + str(count))
  
