class WeekDayError(Exception):
    pass
	

class Weeker:
    allDays = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    

    def __init__(self, day):
        self.today = day
        if(self.today not in self.allDays.values()):
            raise WeekDayError
        else:
            self.pos = (list(self.allDays.keys())[list(self.allDays.values()).index(self.today)])

    def __str__(self):
        return self.today

    def add_days(self, n):
        self.move = n
        self.pos = (self.move + self.pos) % 7
        self.today = self.allDays[self.pos]

    def subtract_days(self, n):
        self.move = n
        self.pos = (self.pos - self.move) % 7
        self.today = self.allDays[self.pos]

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(3)
    print(weekday)
    weekday.subtract_days(4)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
