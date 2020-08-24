import pandas as pd
import numpy as np
import os
import xlsxwriter
from openpyxl import load_workbook

data = np.array([21, 5, 11, 8, 9, 7])
dict_data = {"a": 10, "b": 11, "c": 12}
df = pd.DataFrame(data,columns=["Alphabet"]) # single column dataframe
# df = pd.DataFrame(data, columns=["Alphabet"],
#                   index=["index 1", "index 2", "index 3", "index 4", "index 5",
#                          "index 6"])  # single column dataframe with custom rows
# df["Alphabet"][0:3].to_excel("export_dataframe.xlsx", index=True, header=True)
df["Alphabet"][0:3]  # slice with column
# print(df["Alphabet"][0:3])
# print('series data with label index', pd.Series(data))
# print('series data with over own choice\n',
#       pd.Series(data, index=["index 1", "index 2", "index 3", "index 4", "index 5", "index 6"]))
# print('series data with dictionary label index\n', pd.Series(dict_data,))
# print('data type\n', df.dtypes())
# print('column names and how much rows\n', df.axes())
# print('detect empty rows values return true/false\n', df.empty())
# print('rows amount and column amount\n', df.shape())
# print('total number of rows into dataframe\n', df.size())
# print('data values into array format\n', df.values())
# print('return default 5 rows of dataset\n', df.head())
# print('return default last 5 rows of dataset\n', df.tail())
# print('sum dataset\n', df.sum())
# print('only work on number or float type dataset\n', df.mean())
# print('count rows and detect datatype of dataset\n', df.count())
# print('return min value row of dataset\n', df.min())
# print('return max value rows of dataset\n', df.max())
# print('return sum,mean, max,min, count etc func of dataset\n', df.describe())
print('return default last 5 rows of dataset\n', df.info())
