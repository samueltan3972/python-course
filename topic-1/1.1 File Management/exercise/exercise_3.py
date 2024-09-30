# Exercise 2: Play with file

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here
import os

# Quiz 1: Create a new empty file if not exists
def create_file(file_name):
    # if file_name not exists:
        # create a new empty file with file_name
    pass # Complete the function

create_file("hello.txt") # It should not create any file
create_file("temp.txt") # It should create a new file call "temp.txt"

# Quiz 2: Move the newly created file "temp.txt" into "hello"
# write your code below


print("Move temp.txt into hello:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'temp.txt')))

# Quiz 3: Rename the "temp.txt" file in "hello" to "heyoo.txt"
# write your code below


print("Rename temp.txt into heyoo.txt:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo.txt')))

# Quiz 4: Copy the "heyoo.txt" file in "hello" into parent directory (the current directory)
# write your code below


print("Copy heyoo to parent, check hello:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo.txt')))
print("Copy heyoo to parent, check parent:", os.path.exists(os.path.join(os.getcwd(), 'heyoo.txt')))

# Quiz 5a: Delete "heyoo.txt"
# write your code below

print("Delete heyoo.txt in parent:", os.path.exists(os.path.join(os.getcwd(), 'heyoo.txt')))

# Quiz 5b: Delete "heyoo.txt" file inside "hello"
# write your code below

print("Delete heyoo.txt in hello:", os.path.exists(os.path.join(os.getcwd(), 'hello', 'heyoo.txt')))

