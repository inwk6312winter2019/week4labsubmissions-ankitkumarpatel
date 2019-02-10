"""

The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.
Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages (http://en.wikipedia.org/wiki/Zipf's_law). Specifically, it predicts that the frequency, f, of the word with rank r is:
f = c r−s
where s and c are parameters that depend on the language and the text. If you take the logarithm of both sides of this equation, you get:
logf = logc − s logr
So if you plot log f versus log r, you should get a straight line with slope −s and intercept log c.
Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r. Use the graphing program of your choice to plot the results and check whether they form a straight line. Can you estimate the value of s?
To make the plots, you might have to install matplotlib

"""


import string


hist = dict()
lst = []
def depunctuate(line):
    for punc in string.punctuation:
        line = line.replace(punc, " ")

def histogram(filename):
    file = open(filename)
    for line in file:
        depunctuate(line)
        line = line.split()
        for word in line:
            word = word.strip(string.punctuation+string.whitespace).lower()
            hist[word] = hist.get(word,0)+1
    return(hist)

hist = histogram("mybook.txt")
lst = [(value,key)for key,value in sorted(hist.items())]
print(lst)

