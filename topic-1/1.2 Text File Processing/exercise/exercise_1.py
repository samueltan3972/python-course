# Exercise 1: File Handling (Read, Write, Append)

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here
import os

# Quiz 1: Create a file with name "bonjour.txt"
# write your code below




###############################################
if os.path.isfile("bonjour.txt"):
    print("Quiz 1: Passed")
else:
    print("Quiz 1: Fail")
###############################################

# Quiz 2: Read all the lines in hello.txt and append to the list "content"
# Remember to read the file with utf-8
content = [] # append to this list

# write your code below 




###############################################
if len(content) == 10 and content[-1] == "مرحبًا":
    print("Quiz 2: Passed")
else:
    print("Quiz 2: Fail")
###############################################

# Quiz 3: Write all the line in the list "content" to bonjour.txt with 'w' option
content.append("안녕하세요")

# write your code below




###############################################
try:
    if open("bonjour.txt", "r", encoding="utf-8").readlines()[-1].replace("\n", "") == "안녕하세요":
        print("Quiz 3: Passed")
    else:
        print("Quiz 3: Fail")
except:
    print("Quiz 3: Fail")
###############################################

# Quiz 4: Append "line_to_append" to hello.txt with 'a' option
line_to_append = "こんにちは"

# write your code below




###############################################
try:
    if open("hello.txt", "r", encoding="utf-8").readlines()[-1].replace("\n", "") == "こんにちは":
        print("Quiz 4: Passed")
    else:
        print("Quiz 4: Fail")
except:
    print("Quiz 4: Fail")
###############################################

# Quiz 5: Close the file you open
# write your code below





