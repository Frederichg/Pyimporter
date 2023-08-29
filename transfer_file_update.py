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
import tkinter as tk
from tkinter import filedialog
import os

"""
This open a GUI to browse the folder to import data from then it save it for the next time
	"""

def update(directory,source_directory,destination_directory):

            if __name__ == "__main__":
               # directory = self.lineEdit.text() 
                #directory = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file" # Replace with the path to your directory
                directory =directory
                
                # Source directory containing the Excel files
                source_directory =source_directory

                # Destination directory to copy the files
                destination_directory =destination_directory
                                                         
            try:
                
                source_file_path = "" 
                
                files = os.listdir(directory)
                file_names=files
                all_file_names = []
                if file_names:
                    nb_files={len(file_names)}
                    print(f"Total number of files in the directory: {nb_files}")
                    #print("List of files in the directory:")
                    for file_name in file_names:
                        all_file_names.append(file_name)
                    
                    
                    # Get a list of all Excel files in the source directory
                    excel_files = glob.glob(os.path.join(source_directory, "*.xlsx"))

                    # Filter the list to find files with timestamp in the name
                    timestamp_files = [file for file in excel_files if "_" in os.path.basename(file)]

                    # Sort timestamp_files by modification time
                    timestamp_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

                    # Check if there are timestamp files
                    if timestamp_files:
                        print("deu")
                        most_recent_file = timestamp_files[0]
                        
                        # Get the filename without extension and timestamp
                        file_name, _ = os.path.splitext(os.path.basename(most_recent_file))
                        original_timestamp = file_name.split("_")[-1]

                        # Get the current timestamp
                        current_timestamp = datetime.now().strftime('%Y-%m-%d %H-%M')

                        # Create the new file name with current timestamp
                        new_file_name = f"output_{current_timestamp}.xlsx"

                        # Create the full paths for the source and destination files
                        source_file_path = os.path.join(source_directory, most_recent_file)
                        output_file_name = os.path.join(destination_directory, new_file_name)
                         # Copy the file with the new timestamp to the destination
                        shutil.copy(source_file_path, output_file_name)
                        

                    else:
                        print("No timestamped Excel files found in the source directory.")
                                    
                    
                    for i in range(len(file_names)):
                            print("i has a value of", i)

                            # Replace 'your_value_here' with the actual value you want in the DataFrame
                            value = 0

                            # Create a DataFrame with the specified value in the 'Output' column
                            new_row = {'Output': value, 'Line':i, 'File Name': all_file_names[i]}
                            df_new_row = pd.DataFrame(new_row, index=[0])

                            # Create a timestamp for the output file name
                            if i==0 : 
                                timestamp = datetime.now().strftime('%Y-%m-%d %H-%M')
                            else : 
                                timestamp=timestamp
                            # output_file_name = f'C:\\Users\\tutag\\OneDrive\\Documents\\final_file\\output_{timestamp}.xlsx'

                            output_file_name = f'C:\\Users\\pfh3221\\Documents\\destination\\output_{timestamp}.xlsx'

                       
                            if os.path.isfile(output_file_name):
                                        # If the file already exists, open it and append data
                                    existing_df = pd.read_excel(output_file_name)
                                            
                                        # Check if the File Name already exists in the DataFrame
                                    if all_file_names[i] in existing_df['File Name'].tolist():
                                        print(f'File Name {all_file_names[i]} already exists in the DataFrame.')
                                    else:
                                        updated_df = pd.concat([existing_df, df_new_row], ignore_index=True)
                                        updated_df.to_excel(output_file_name, index=False)
                            else:
                                    # If the file doesn't exist, use the new DataFrame
                                    df_new_row.to_excel(output_file_name, index=False)

                                    print(f'Output written to {output_file_name}')
                        
                                    print(f"File copied from {source_file_path} to {output_file_name}")
                      
                
                else:
                    print("No files found in the directory.")
                print("All file names:", all_file_names)
                
              
            except Exception as e:
                print(f"Error reading directory: {e}")
                return []