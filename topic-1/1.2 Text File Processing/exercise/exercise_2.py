# Exercise 2: CSV, JSON, and XML File

# Answer the quiz and write your code in this file
# -------------------------------------------- #

# Import library here
import os

# Quiz 1: Read the sample/sample.csv file and write the content into customer.txt with the following structure
# {last name}, {first name} lives in {city}, {country}
# Example: Baxter, Sheryl lives in East Leonard, Chile

# write your code below




###############################################
if os.path.isfile("customer.txt") and len(open('customer.txt').readlines()) == 100:
    print("Quiz 1: Passed")
else:
    print("Quiz 1: Fail")
###############################################

# Quiz 2: Read the sample/sample.json file and write the content into language.txt with the following structure
# {name} speaks {language}, {name} said {bio}.
# Example: Adeel Solangi speaks Sindhi, Adeel Solangi said Donec lobortis ele...

# write your code below




###############################################
if os.path.isfile("language.txt") and len(open('language.txt').readlines()) == 197:
    print("Quiz 2: Passed")
else:
    print("Quiz 2: Fail")
###############################################

# Quiz 3: Read the sample/sample.xml file and save the name of the employee into employee.txt
# write your code below




###############################################
if os.path.isfile("employee.txt") and len(open('employee.txt').readlines()) == 206:
    print("Quiz 3: Passed")
else:
    print("Quiz 3: Fail")
###############################################