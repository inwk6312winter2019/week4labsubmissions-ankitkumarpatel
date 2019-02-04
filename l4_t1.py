"""
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
"""
import string 

file=open("mybook.txt")

for line in file:
    line = line.split()
    for word in line:
        word = word.strip(string.punctuation+string.whitespace).lower()
        print(word)   
