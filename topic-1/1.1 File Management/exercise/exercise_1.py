# Exercise 1: Navigating the file path

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here

entries = ""
filepath = ""
current_file_path = ""
is_current_file_path = ""
is_filepath = ""

# Quiz 1: Get the current file path (Uncomment the line below and write your code)
# current_file_path = 
print("Current file path: ", current_file_path)

# Quiz 2: List all the file and directory in the current file path
# entries = # uncomment and write your code
print("List all file and directory:", entries)

filename = "hello.txt"

###############################################

# Quiz 3a: Concat the current_file_path with filename by hand
# filepath = # uncomment and write your code

# Quiz 3b: Concat the current_file_path with filename using os.path
# filepath = # uncomment and write your code

# Quiz 3c: Concat the current_file_path with filename using pathlib
# filepath = # uncomment and write your code

print("Concatenated file path: ", filepath)

###############################################

# Quiz 4a: Check whether current_file_path is a folder
is_current_file_path = current_file_path # modify this line
print("Is current_file_path is folder:", is_current_file_path)

# Quiz 4b: Check whether current_file_path is a file
is_current_file_path = current_file_path # modify this line
print("Is current_file_path is file:", is_current_file_path)

###############################################

# Quiz 5a: Check whether filepath is a folder
is_filepath = filepath # modify this line
print("Is filepath is folder:", is_filepath)

# Quiz 5b: Check whether filepath is a file
is_filepath = filepath # modify this line
print("Is filepath is file:", is_filepath)
