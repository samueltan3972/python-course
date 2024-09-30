# Exercise 3: String Operation

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here


text = ''
country_list = []

# Quiz 1: Read the content in sample/sample.txt into "text"
# write your code below




###############################################
if text != "":
    print("Quiz 1: Passed")
else:
    print("Quiz 1: Fail")
###############################################

# Quiz 2: Make the content in "text" into UPPERCASE
# write your code below




###############################################
if text.isupper():
    print("Quiz 2: Passed")
else:
    print("Quiz 2: Fail")
###############################################

# Quiz 3: Remove all "." in text
# write your code below




###############################################
if '.' not in text and text != "":
    print("Quiz 3: Passed")
else:
    print("Quiz 3: Fail")
###############################################

# Quiz 4: Split the "text" with newline character '\n' and extract the country and append into "country_list"
# newline character '\n' is character that makes a new line, just like "enter" key
# write your code below




###############################################
answer = ['AUSTRALIA', 'AUSTRIA', 'BELGIUM', 'BRAZIL', 'CANADA', 'ECUADOR', 
          'FIJI', 'FRANCE', 'ITALY', 'MEXICO', 'NETHERLANDS', 'PERU', 'REPUBLIC', 
          'SPAIN', 'SWITZERLAND', 'UK', 'USA', 'WALES']
if country_list == answer:
    print("Quiz 4: Passed")
else:
    print("Quiz 4: Fail")
###############################################