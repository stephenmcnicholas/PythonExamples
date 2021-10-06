from calendar import Calendar  

class MyCalendar(Calendar):

    def __init__(self):
        Calendar.__init__(self)
 
    def count_weekday_in_year(self, yr, day):
        self.weekday = day
        self.year = yr        
        c = Calendar()
        cnt = 0
        for qtr in c.yeardays2calendar(self.year):
            for month in qtr:
                for week in month:
                    for day in week:
                        if day[0]>0:
                            if day[1]==self.weekday:
                                cnt+=1
        return cnt

myCal = MyCalendar()
days = myCal.count_weekday_in_year(2000, 6)
print(days)
