'''This part of the code is to open a GUI to browse the folder to import data from then it save it for the next time'''
def get_all_filename(file_names):
    
    import tkinter as tk
    from tkinter import filedialog
    import os
    import pandas as pd

# Set the directory path
    directory_path = file_names #"/path/to/your/folder"

# Get a list of all file names in the directory
    file_names = os.listdir(directory_path)

# Create a Pandas DataFrame with the file names
    df = pd.DataFrame(file_names, columns=["file_name"])
    return df
