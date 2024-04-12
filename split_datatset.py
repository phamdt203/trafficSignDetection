import os
import random
import shutil

image_folder = r"data\images"
label_folder = r"data\labels"

train_folder = r"final_data\train\labels"
val_folder = r"final_data\valid\labels"
test_folder = r"final_data\test\labels"

train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

image_files = os.listdir(label_folder)
random.shuffle(image_files)

train_split = int(len(image_files) * train_ratio)
val_split = int(len(image_files) * (train_ratio + val_ratio))

train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]

def move_files(files, src_folder, dest_folder):
    for file in files:
        src_path = os.path.join(src_folder, file)
        dest_path = os.path.join(dest_folder, file)
        shutil.move(src_path, dest_path)

move_files(train_files, label_folder, train_folder)
move_files(val_files, label_folder, val_folder)
move_files(test_files, label_folder, test_folder)
