import os, glob

os.chdir("/Users/principal/Downloads")

for file in glob.glob("*.*"):
    print(file)