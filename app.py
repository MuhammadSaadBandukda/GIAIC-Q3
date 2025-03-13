import pandas as pd
import os
a = os.path.splitext("abs.xyz")[1]
print(type(a))


# Get the current working directory
print(os.getcwd())  # e.g., "C:\Users\YourName"

# List files in a directory
print(os.listdir("."))  # Lists files in the current directory

# Check if a file exists
print(os.path.exists("document.pdf"))  # True or False

# Create a new folder
os.mkdir("new_folder")
