class Time:

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def get_time(self):
        return f"{self.hours:>02}:{self.minutes:>02}:{self.seconds:>02}"

    def next_second(self):
        self.seconds += 1
        return self.get_time()

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int):
        self.__seconds = seconds
        if self.__seconds > Time.max_seconds:
            self.__seconds = 0
            self.minutes += 1

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes
        if self.__minutes > Time.max_minutes:
            self.__minutes = 0
            self.hours += 1

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours
        if self.__hours > Time.max_hours:
            self.hours = 0

time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(16, 35, 54)
time.set_time(1,20,30)
print(time.get_time())
print(time.next_second())