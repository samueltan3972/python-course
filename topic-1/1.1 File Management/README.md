## 1.1 File Managment with Python

In this sub topic, we will looks at how can we use python to deal with file and folder. Before we going into file management such as create, delete, or rename any file or folder, we will first look into file path.

Remember your last time you going to a shopping mall with your car, and you park your car at the car park, you saw text like B1-J04, it possibly means you park the car at level of B1, at the place of J04. The text you saw will give you an idea where you put your park your car. 

![image.png](../../assets/topic-1-carpark.png)

Let’s say you are having a pdf file in your computer, the file is like your car where you have to put the file at somewhere in the computer (car park). Hopefully, when you save your file in the computer, you might saw some text like C:\Users\user\Desktop. That text is like the text you saw in the car park, where it tell you the location of the file, in this case it is call file path.

Depends on the computer you using, the file path might looks different depends on the Operating System (OS) your computer running, whether it is Windows, MacOS (if you are using MacBook), or Linux. 

Windows is the most commonly found OS, where the file path looks like C:\Users\file.pdf, where C: refers to the drive.

MacOS and Linux is having similar looks on the file path, where it might looks like /home/user/file.pdf, where the file path start with “/” instead of “C:”. 

So now, you might ask why do we need to look at the file path first? Let’s get back to the analogy above, now you are done with the shopping, and wish go back home. But first, you will need to get to your car. It is the same in this case, before you dealing with any file, you have to get to the correct file path or directory, before you do anything with the file. Without getting to the right file path, you won’t be able to do anything with the file, just like you won’t be able to drive the car, until you get into your car. Therefore, if you getting any error when you are dealing with file, the first thing you should check is whether you are in the correct file path.

### Your reading:

1. [Python 3 Quick Tip: The easy way to deal with file paths on Windows, Mac and Linux | by Adam Geitgey | Medium](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)
2. [Working With Files in Python – Real Python](https://realpython.com/working-with-files-in-python/#traversing-directories-and-processing-files) 
3. [How to Create, Move, and Delete Files in Python (stackabuse.com)](https://stackabuse.com/how-to-create-move-and-delete-files-in-python/) - Take note on file opening modes
4. [File Organizing with Python: Rename, Move, Copy & Delete Files and Folders (youtube.com)](https://www.youtube.com/watch?v=NOvFZamGXXo)
5. [Check if directory or file exists](https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python)

### Exercise/Quiz
1. Download/Clone the repository, you exercise is in the [exercise folder](exercise).
2. For exercise, follow in instruction complete the code in [exercise_1.py](exercise/exercise_1.py), [exercise_2.py](exercise/exercise_2.py), and [exercise_3.py](exercise/exercise_3.py).
3. See [expected_output](exercise/expected_output/) folder to check on your answer.

### Challenge
1. Download/Clone the repository, you challenge question is in the [challenge folder](challenge/question.txt).
2. Read the [question.md](challenge/question.md) for instruction.
3. Write the code to complete the challenge, use the files in "images" folder for your challenge.
4. Run [validate_answer.py](challenge/validate_answer.py) to validate your answer. It should pass all the tests.
    ```python
    python3 validate_answer.py
    ```

### Reference Learning Notes
[Learning Notes](learning_notes.py) for your reference. For quick learning without going through the reading, going though the reading material is still highly recommended.
