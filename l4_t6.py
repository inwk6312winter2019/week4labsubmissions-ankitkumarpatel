"""
The os module provides a function called walk that is similar to one below but more versatile. Read the documentation and use it to print the names of the files in a given directory and its subdirectories.

"""
import os

os.chdir("/home/student/Documents/ankit")

for root,dirs,files in os.walk(".",topdown = False):

    for name in files:
        print(os.path.join(root,name))


    for name in dirs:
        print(os.path.join(root,name))