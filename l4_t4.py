"""
Modify the previous program to read a word list and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are obscure?
Python provides a data structure called set that provides many common set operations. Read the documentation and write a program that uses set subtraction to find words in the book that are not in the word list.

"""


import string


hist = dict()
lst = []


def histogram(filename):
    file = open(filename)
    for line in filename:
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation+string.whitespace).lower()
            hist[word] = hist.get(word,0)+1
    return(hist)

def difference(t,w):
    set_t = set(t)
    set_w = set(w)
    set_diff = set_t.difference(set_w)
    f"printing all the words in the book that are not in the word list:"
    print(set_t)
    print(set_w)
    print(set_diff)



text_histo = histogram("mybook.txt")
word_histo = histogram("words.txt")
print(text_histo)
print(word_histo)
difference(text_histo,word_histo)


