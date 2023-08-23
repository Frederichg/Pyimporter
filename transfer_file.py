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
nb_files=100




class MyGUI(QMainWindow): 
    def __init__(self) :
        super(MyGUI,self).__init__ ()
        uic.loadUi("mygui.ui",self)
        self.show()
        
        self.pushButton.clicked.connect(self.browser)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.transfer)
        
    def browser(self): 
        
        
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
        




            # try:
            #     # Get the user's home directory
            #     user_home = os.path.expanduser("~")

            #     # Path to the Documents folder
            #     documents_path = os.path.join(user_home)
                
            #     #directory_path = "C:\\Users\\tutag\\OneDrive\\Documents\\PROJETJAVA" 
            #     os.system(f'explorer "{documents_path}"')  # For Windows
            #     # For macOS, use: os.system(f'open "{directory_path}"')
            #     # For Linux, use: os.system(f'xdg-open "{directory_path}"')
            #     print(f"Opened directory: {documents_path}")
            # except Exception as e:
            #     print(f"Error: {e}")

    
    def update(self): 
        
            if __name__ == "__main__":
               # directory = self.lineEdit.text() 
                #directory = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file" # Replace with the path to your directory
                directory =self.good_directory
                                
            try:
                files = os.listdir(directory)
                file_names=files
                all_file_names = []
                if file_names:
                    nb_files={len(file_names)}
                    print(f"Total number of files in the directory: {nb_files}")
                    #print("List of files in the directory:")
                    for file_name in file_names:
                        all_file_names.append(file_name)
                    
                    value=0
                    for i in range(len(file_names)):
                        print("i has a value of", i)


                        # Replace 'your_value_here' with the actual value you want in the DataFrame
                        value = 0

                        # Create a DataFrame with the specified value in the 'Output' column
                        new_row = {'Output': value, 'Line':i, 'File Name': all_file_names[i]}
                        df_new_row = pd.DataFrame(new_row, index=[0])

                        # Create a timestamp for the output file name
                        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                        output_file_name = f'C:\\Users\\tutag\\OneDrive\\Documents\\final_file\\output_.xlsx'

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
                
                else:
                    print("No files found in the directory.")
                print("All file names:", all_file_names)
                
              
            except Exception as e:
                print(f"Error reading directory: {e}")
                return []
                
      
    def transfer(self):
        source_directory = self.good_directory  # Replace with the source directory path
                
        destination_directory = "C:\\Users\\tutag\\OneDrive\\Documents\\final_file"  # Replace with the destination directory path

        # Get a list of all files in the source directory
        file_list = os.listdir(source_directory)

        for filename in file_list:
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)

            # Copy the file from source to destination
            
            shutil.copy(source_path, destination_path)
            

            
            print(f"File {filename} copied to {destination_directory}")



def main() :
    app = QApplication([])
    window = MyGUI()
    app.exec_()

    

    
main()