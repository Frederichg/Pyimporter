'''This part is the one that is taking the name of all the files, then put their name on the Index'''

import os
import pandas as pd

# List all CSV files
csv_files = [f for f in os.listdir("/data/") if f.endswith(".csv")]

# Extract names without extensions
csv_names = [os.path.splitext(f)[0] for f in csv_files]

# Open Index2.xlsx and get first column
index_df = pd.read_excel("data/Index2.xlsx")
index_column = index_df.iloc[:, 0].tolist()

# Find new names to add
new_names = [name for name in csv_names if name not in index_column]

# Append (add at the end) new names to the dataframe
for name in new_names:
    index_df = index_df.append({index_df.columns[0]: name}, ignore_index=True)

# Save updated Index2.xlsx
index_df.to_excel("/data/Index2.xlsx", index=False)
