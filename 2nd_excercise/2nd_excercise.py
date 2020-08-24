import pandas as pd
import numpy as np
import os, sys
import xlsxwriter
from openpyxl import load_workbook

# newfile=os.path.join(pth,'combined.xlsx') # Todo: save file any other directory
file = os.path.join('../demo_sheets/SampleData.xlsx')
data = pd.read_excel(file)
df = pd.DataFrame(data)
# print(df[(df['Units'] == 27) & (df['Rep'] == 'Gill')])
print(df[df['Units'] > 80])
