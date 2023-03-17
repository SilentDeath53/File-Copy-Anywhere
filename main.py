import os
import shutil

root_dir = '/path/to/root/directory'
file_to_copy = 'file_to_copy.txt'

for subdir, dirs, files in os.walk(root_dir):
    for dir in dirs:
        subdir_path = os.path.join(subdir, dir)
        shutil.copy(file_to_copy, subdir_path)
