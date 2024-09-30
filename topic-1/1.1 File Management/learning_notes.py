# 1.1 File Management Learning Notes
# 1. File Opening
# Read from file
with open("hello.txt", mode='r', encoding="utf-8") as f:
    data = f.read()
    print(data)

# Write to file
with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)

###########################################

# 2. Directory Listing
# 2a. Legacy way
import os
entries = os.listdir(os.getcwd())
print(entries)

# 2b. Modern way - return as iterator
import os

with os.scandir(os.getcwd()) as entries:
    for entry in entries:
        print(entry.name)
    print()

# 2c. pathlib way - return as iterator
from pathlib import Path

entries = Path(os.getcwd())
for entry in entries.iterdir():
    print(entry.suffix)

###########################################

# 3. Create directory
# 3a. Create single directory
import os

os.mkdir('example_directory/', exist_ok=True) # throw OSError if exists_ok=False
os.makedirs('2018/10/05') # Create nested directories

# 3c. Using pathlib
from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True) # throw FileExistsError if exists_ok = False

p = Path('2018/10/05')
p.mkdir(parents=True) # nested directory

# 4. Filename matching with string, fnmatch, glob

###########################################

# 5. Traverse directory recursively
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

###########################################

# 6. Temporary file and directories
from tempfile import TemporaryFile

# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')
fp.write('Hello universe!')

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()

# Close the file, after which it will be removed
fp.close()

import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    print('Created temporary directory ', tmpdir)
    os.path.exists(tmpdir)

os.path.exists(tmpdir) # False, tmpdir is not available anymore here

###########################################

# 7. Delete file
import os

os.remove("data.txt")
os.unlink("data.txt") # throw OSError if it is directory

# pathlib way
data_file = Path('home/data.txt')
data_file.unlink()

###########################################

# 8. Delete directory
os.rmdir('my_documents/bad_dir')
os.removedirs('') # remove recursively

# pathlib way
trash_dir = Path('my_documents/bad_dir')
trash_dir.rmdir('abc')

# delete non empty directory
import shutil

trash_dir = 'my_documents/bad_dir'
shutil.rmtree(trash_dir)

# delete empty directory only recursively
import os

for dirpath, dirnames, files in os.walk('abc', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError as ex:
        pass

###########################################

# 9. Copy, Move, Rename
import shutil

shutil.copy('src/file.txt', 'dst/file.txt')
shutil.copy2('src/file.txt', 'dst/file.txt') # preserve meta data
shutil.copytree('data_1', 'data1_backup') # directory

# move
shutil.move('dir_1/', 'backup/')

# rename
os.rename('first.zip', 'first_01.zip')

data_file = Path('data_01.txt')
data_file.rename('data.txt')

###########################################

# 10. Change directory
os.chdir('/')

###########################################

# 11. Path concat
# Quiz 3a: Concat the current_file_path with filename by hand
filepath = os.getcwd() + '\\' + "hello.txt"

# Quiz 3b: Concat the current_file_path with filename using os.path
filepath = os.path.join(os.getcwd(), "hello.txt")

# Quiz 3c: Concat the current_file_path with filename using pathlib
filepath = Path(os.getcwd()) / "hello.txt"

###########################################

# 12. Checking file and directory
os.path.isdir('mydir')
os.path.isfile('mydir')
os.path.exists('mydir')