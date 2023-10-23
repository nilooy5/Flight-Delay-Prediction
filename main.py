import os

import pandas as pd

# make a list of subfolders in the data folder
# and sort them
folders = os.listdir("data")
folders.sort()
data = []

for folder in folders:
    # make a list of files in the subfolder
    # and sort them
    files = os.listdir("data/" + folder)
    files.sort()
    for file in files:
        if file.endswith(".csv"):
            print("data/" + folder + "/" + file)
            data.append(pd.read_csv("data/" + folder + "/" + file))


print(data.head())