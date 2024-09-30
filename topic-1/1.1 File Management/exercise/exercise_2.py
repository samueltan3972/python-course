# Exercise 2: Play with directory

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here
import os

# Quiz 1: Create a new folder if not exists
def create_folder(folder_name):
    # if folder_name not exists:
        # create a new folder with folder_name
    pass # Complete the function

create_folder("hello") # It should not create any folder
create_folder("temp2") # It should create a new folder call "temp2"
create_folder("temp") # It should create a new folder call "temp"

# Quiz 2: Move the newly created folder "temp" into "hello"
# write your code below


print("Move temp into hello:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'temp')))

# Quiz 3: Rename the "temp" folder in "hello" to "heyoo"
# write your code below


print("Rename temp into heyoo:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo')))

# Quiz 4: Copy the "heyoo" folder in "hello" to "temp2"
# write your code below


print("Copy heyoo to temp2, check hello:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo')))
print("Copy heyoo to temp2, check temp2:", os.path.exists(os.path.join(os.getcwd(), 'temp2', 'heyoo')))

# Quiz 5a: Delete "temp2" folder
# write your code below

print("Delete temp2:", os.path.exists(os.path.join(os.getcwd(), 'temp2')))

# Quiz 5b: Delete "heyoo" folder inside "hello"
# write your code below

print("Delete heyoo:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo')))

