#importing library
import math

# other style of import
import math as m
from math import *
from math import pi, cos

# using built-in variable
print(math.pi)

# using built-in function
print(math.cos(math.pi*2))


# Using library to work with excel file

import openpyxl as xl

# open workbook
wb = xl.load_workbook("example/example.xlsx")

# print sheet names
print(wb.sheetnames)

# open sheet
sheet_1 = wb['Sheet1']

# read value from file
print(sheet_1.cell(1,1).value)

# write value to cell
sheet_1.cell(4,1, "Yessy M")

# show name of tables in a sheet
print(sheet_1.tables.keys())

# save file
wb.save("example/example.xlsx")

# close workbook to save memory
wb.close()