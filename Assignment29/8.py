# 8. Write a Python script to create a copy of a file.

import shutil

original = r'D:\Java Programs\Accesser Mutator'
target = r'D:\Python'

shutil.copyfile(original, target)
