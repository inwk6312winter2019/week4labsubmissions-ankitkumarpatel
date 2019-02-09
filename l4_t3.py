"""

Modify the program from the previous exercise to print the 20 most frequently-used words in the book.


"""


import string

file=open("mybook.txt")

#count=0
hist = dict()
lst = []
for line in file:
    line = line.split()
    for word in line:
        word = word.strip(string.punctuation+string.whitespace).lower()
        #count +=1
        hist[word] = hist.get(word,0)+1

       # print(word)
print("Total number of words are %d" % sum(hist.values()))
#print(count)

print("Total number of different words are %d" % len(hist))

lst = [(value,key)for key,value in hist.items()]
lst.sort(reverse=True)
for item in lst[:20]:
    print(item)