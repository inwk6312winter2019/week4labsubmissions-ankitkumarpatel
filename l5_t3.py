"""

Write a function called print_time that takes a Time object and prints it in the form hour:minute:second. Hint: the format sequence '%.2d'prints an integer using at least two digits, including a leading zero if necessary. Bonus: Try to use the “format” method of String objects

"""


class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second


def print_time(t):

    print('%.2d:%.2d:%.2d'.format(t.hour, t.minute, t.second))

time = Time(10,10,10)
print_time(time)