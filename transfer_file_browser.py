from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
from datetime import datetime
import pandas as pd
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import os
nb_files=10
import glob


"""
This open a GUI to browse the folder to import data from then it save it for the next time
	"""

def browser():

    import tkinter as tk
    from tkinter import filedialog
    import os	
    

# Create a root window to hide

    root = tk.Tk()

    root.withdraw()

# Set the initial directory to the last-used directory, or the current working directory if none

    last_directory_file = 'last_directory.txt'

    if os.path.exists(last_directory_file):

        with open(last_directory_file, 'r') as f:

            initial_directory = f.read().strip()

    else:

        initial_directory = os.getcwd()

# Open a file dialog box to select a directory

    selected_directory = filedialog.askdirectory(initialdir=initial_directory)

# Save the selected directory as the last-used directory

    with open(last_directory_file, 'w') as f:

        f.write(selected_directory)

# Use the selected directory in your code

    print(f"The selected directory is: {selected_directory}")
    return selected_directory













""" 

        
    def browser(): 
        
        
            # Create a root window to hide

            root = tk.Tk()

            root.withdraw()

            # Set the initial directory to the last-used directory, or the current working directory if none

            last_directory_file = 'last_directory.txt'

            if os.path.exists(last_directory_file):

                with open(last_directory_file, 'r') as f:

                    initial_directory = f.read().strip()

                else:

                initial_directory = os.getcwd()

            # Open a file dialog box to select a directory

                selected_directory = filedialog.askdirectory(initialdir=initial_directory)

            # Save the selected directory as the last-used directory

                with open(last_directory_file, 'w') as f:

                    f.write(selected_directory)

        # Use the selected directory in your code

            print(f"The selected directory is: {selected_directory}")
            self.good_directory =selected_directory 
        
    """