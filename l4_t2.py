"""
Modify your program from the previous exercise to read the book you downloaded, , and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times each word is used.
Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary? 
Bonus: write a function that takes in any number of books and produce the book with the most number of words
"""

import string 

file=open("mybook.txt")

count=0
hist = dict()
for line in file:
    line = line.split()
    for word in line:
        word = word.strip(string.punctuation+string.whitespace).lower()
        count +=1
        hist[word] = hist.get(word,0)+1

        print(word)
print("Total number ofwords are %d" % sum(hist.values()))
print(count)

