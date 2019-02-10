"""
Write a function called sed  that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
If an error occurs while opening, reading, writing, or closing files, your program should catch the exception, print an error message, and exit.

"""
def sed(pattern,replacement,fileread,filewrite):
    try:
        fin = open(fileread,'r')
        fout = open(filewrite, 'w')
        for line in fin:
            if pattern in line:
                print(line)
                line = line.replace(pattern,replacement)
                print(line)
            fout.write(line)
    except:
        print("Something wrong happenned while replacement!!!")
    finally:
        print("Good bye!!!")



sed('The','WOW','smallbook.txt','temp.txt')