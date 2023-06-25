'''this opens the files'''
def load_file(returned_path, file_name): #: probably add the paht to file then cocatenate it 
    import xlwings as xw
    import pandas as pd
    import numpy as np

    path_file_name = returned_path + "/" + file_name
    print(path_file_name)
    # data2 = pd.read_csv(r'C:\Users\pfh3221\OneDrive - Université de Moncton\Électronics et al\Programmes Matlab analyse\INPUTPCA\2020_12_23__17_32_06_135.csv', delimiter=',', skiprows=9, usecols=range(6))
    data2 = pd.read_csv(path_file_name, delimiter=',', skiprows=9, usecols=range(6)) #: probablement cocaténation

    #xw.view(data2)

    xw.view(obj = data2, table = True)  #this Table is for having blue and white

    #xw.Book()

    xw.books.active

    # wx.books.active.close()

    # wb.close()

    sheet = xw.sheets[0]
        # print(A)
    sheet.range('B4').value = 10
    A = sheet.range('B4').value
    print(A)
    
    return (A)