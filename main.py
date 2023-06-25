'''test de test'''

import importgui as ig
import loadfile as lf
import get_all_filename as gf

returned_path = ig.import_gui()
all_names_files = gf.get_all_filename(returned_path)
# print(all_names_files(1, 1))

file_name = all_names_files.at[10, 'file_name']
# print(value)

B = lf.load_file(returned_path, file_name)
# print(B)


#TODO: ADD names to the index file after the last value
#TODO: Cut the files from the origin and paste them at the depot