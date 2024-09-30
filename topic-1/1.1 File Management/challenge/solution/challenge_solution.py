import zipfile
import os
import shutil

from pathlib import Path

with zipfile.ZipFile("images.zip","r") as zip_ref:
    zip_ref.extractall("")

try:
    os.makedirs("dataset/training/accident")
    os.makedirs("dataset/training/non-accident")
    os.makedirs("dataset/validation/accident")
    os.makedirs("dataset/validation/non-accident")
    os.makedirs("dataset/testing/accident")
    os.makedirs("dataset/testing/non-accident")
except OSError as err:
    pass

entries = Path('images')
accident_count = 1
non_accident_count = 1
accident_len = len([name for name in os.listdir('images') if name.startswith('accident')])
non_accident_len = len([name for name in os.listdir('images') if name.startswith('non-accident')])

for entry in entries.iterdir():
    if entry.suffix == ".jpg":
        if entry.name.startswith("accident"):
            if accident_count <= round(accident_len * 0.7): # training set
                dst_dir = Path(f"dataset/training/accident/{accident_count}{entry.suffix}")
            elif accident_count <= round(accident_len * 0.8): # validataion set
                dst_dir = Path(f"dataset/validation/accident/{accident_count - int(accident_len * 0.7)}{entry.suffix}")
            else: # testing set
                dst_dir = Path(f"dataset/testing/accident/{accident_count - int(accident_len * 0.8)}{entry.suffix}")

            shutil.move(entry.resolve(), dst_dir)
            accident_count += 1

        if entry.name.startswith("non-accident"):
            if non_accident_count <= round(non_accident_len * 0.7): # training set
                dst_dir = Path(f"dataset/training/non-accident/{non_accident_count}{entry.suffix}")
            elif non_accident_count <= round(non_accident_len * 0.8): # validataion set
                dst_dir = Path(f"dataset/validation/non-accident/{non_accident_count - int(non_accident_len * 0.7)}{entry.suffix}")
            else: # testing set
                dst_dir = Path(f"dataset/testing/non-accident/{non_accident_count - int(non_accident_len * 0.8)}{entry.suffix}")

            shutil.move(entry.resolve(), dst_dir)
            non_accident_count += 1
    else:
        os.remove(entry.resolve())

os.rmdir('images')



