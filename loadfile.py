def load_file():

    import xlwings as xw
    import pandas as pd
    import numpy as np

data2 = pd.read_csv(r'C:\Users\pfh3221\OneDrive - Université de Moncton\Électronics et al\Programmes Matlab analyse\INPUTPCA\2020_12_23__17_32_06_135.csv', delimiter=',', skiprows=9, usecols=range(6))

#xw.view(data2)

xw.view(obj = data2, table = True)  #this Table is for having blue and white

#xw.Book()

# xw.books.active

# wx.books.active.close()

# wb.close()

# sheet = wb.sheets[0]

print(A)

sheet.range('B4').value = 10

A = sheet.range('B4').value

display(A)