# Topic 1.1 - File Management Challenge
The images folder contain images dataset for accident classification. The accident classification consists of two class type:
- accident
- non accident

This is a classification task. You are required to tidy the file and make it into train ready accident classification dataset.

### Instruction
1. Unzip the images.zip
2. Move the accident images in the "images" folder to relevant directory, and rename the file to 1.jpg, 2.jpg, ..., etc.
3. Move the non-accident images in the "images" folder to relevant directory, and rename the file to 1.jpg, 2.jpg, ..., etc.
4. Delete the unnecessary file.
5. Split the dataset into training, validation, and testing set with 7:1:2 ratio. 

### Rules  
1. Do not use sklearn, or other preprocessing library. You are only allowed to use file management related library such as os, pathlib, shutil, etc.
2. Use python code only. No manual work or other tools.

### Result
Your result should looks like this:
```
- dataset
    |- training
        |- accident
            |- 1.jpg
            |- 2.jpg
            | ...
        |- non-accident
            |- 1.jpg
            |- 2.jpg
            | ...
    |- validation
        |- accident
            |- 1.jpg
            |- 2.jpg
            | ...
        |- non-accident
            |- 1.jpg
            |- 2.jpg
            | ...
    |- testing
        |- accident
            |- 1.jpg
            |- 2.jpg
            | ...
        |- non-accident
            |- 1.jpg
            |- 2.jpg
            | ...
```

### Validate the answer
Run validate_answer.py to validate your answer. It should pass all the test.

```python
python3 validate_answer.py
```