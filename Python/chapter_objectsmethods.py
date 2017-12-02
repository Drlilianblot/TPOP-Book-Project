class Time(object):
    """represents the time of day.
       attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


    def print_time(self):
        print('%.2d:%.2d:%.2d' %
              (self.hour, self.minute, self.second))

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __str__(self):
        return ('%.2d:%.2d:%.2d'
                % (self.hour, self.minute, self.second))

##    def __add__(self, other):
##        if isinstance(other, Time):
##            return self.add_time(other)
##        else:
##            return self.increment(other)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        elif (isinstance(other, int)
                  and not isinstance(other, bool)):
            return self.increment(other)
        else:
            raise TypeError("can't add Time with " +
                            type(other).__qualname__)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


def int_to_time(seconds):
    time_minutes, time_seconds = divmod(seconds, 60)
    time_hours, time_minutes = divmod(time_minutes, 60)
    return Time(time_hours, time_minutes, time_seconds)


start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
##print(start + True)
print(start + 1.5)
print(start + '1')

