from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
from datetime import datetime
import pandas as pd
import os
from transfer_file_browser import browser
from transfer_file_transfer import transfer
from transfer_file_update import update
import shutil
import tkinter as tk
from tkinter import filedialog
import os
nb_files=10
import glob

class MyGUI(QMainWindow): 
    def __init__(self) :
        super(MyGUI,self).__init__ ()
        uic.loadUi("mygui.ui",self)
        self.show()
        
        self.pushButton.clicked.connect(self.browser)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.transfer)
        
    def browser(self): 
   
        self.good_directory =browser()
    
    def update(self): 
        update(self.good_directory,"C:\\Users\\pfh3221\\Documents\\destination","C:\\Users\\pfh3221\\Documents\\destination")
  
                
      
    def transfer(self):
     transfer(self.good_directory,"C:\\Users\\pfh3221\\Documents\\destination")  # Replace with the destination directory path




def main() :
    app = QApplication([])
    window = MyGUI()
    app.exec_()

    
main()