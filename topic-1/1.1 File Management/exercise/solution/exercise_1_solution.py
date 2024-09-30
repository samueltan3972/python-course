# Exercise 1: Navigating the file path

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here
import os
from pathlib import Path

entries = ""
filepath = ""
current_file_path = ""
is_current_file_path = ""
is_filepath = ""

# Quiz 1: Get the current file path (Uncomment the line below and write your code)
current_file_path = os.getcwd()
print("Current file path: ", current_file_path)

# Quiz 2: List all the file and directory in the current file path
entries = os.listdir(os.getcwd())
print("List all file and directory:", entries)

filename = "hello.txt"

###############################################

# Quiz 3a: Concat the current_file_path with filename by hand
filepath = current_file_path + '\\' + filename

# Quiz 3b: Concat the current_file_path with filename using os.path
filepath = os.path.join(current_file_path, filename)

# Quiz 3c: Concat the current_file_path with filename using pathlib
filepath = Path(current_file_path) / filename

print("Concatenated file path: ", filepath)

###############################################

# Quiz 4a: Check whether current_file_path is a folder
is_current_file_path = os.path.isdir(current_file_path)
print("Is current_file_path is folder:", is_current_file_path)

# Quiz 4b: Check whether current_file_path is a file
is_current_file_path = os.path.isfile(current_file_path)
print("Is current_file_path is file:", is_current_file_path)

###############################################

# Quiz 5a: Check whether filepath is a folder
is_filepath = os.path.isdir(filepath)
print("Is filepath is folder:", is_filepath)

# Quiz 5b: Check whether filepath is a file
is_filepath = os.path.isfile(filepath)
print("Is filepath is file:", is_filepath)
