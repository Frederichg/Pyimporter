'''This is the part that will move the .csv file to the new location'''
'''Need to make it as a function that will reveive all the file name'''


import shutil

# Create new directory if it doesn't exist
#if not os.path.exists("/data/Repo"):
#    os.makedirs("/data/Repo")

# Move new files to the new directory
for name in new_names:
    shutil.move(f"/data/{name}.csv", f"/data/Repo/{name}.csv")
