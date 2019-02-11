"""

Write a boolean function called is_after that takes two Time objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement.

"""

class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def print_time(t):

    print(('{0:02d}:{1:02d}:{2:02d}').format(t.hour, t.minute, t.second))


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


time1 = Time()
time1.hour = 11
time1.minute = 59
time1.second = 30

time2 = Time()
time2.hour = 14
time2.minute = 45
time2.second = 20
