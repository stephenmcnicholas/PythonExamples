class Timer:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
        

    def __str__(self):
        fH = format(self.hour, '02')
        fM = format(self.min, '02')
        fS = format(self.sec, '02')
        time = fH + ':' + fM + ":" + fS
        return time

    def next_second(self):
        self.sec +=1
        if(self.sec>59):
            self.sec = 0
            self.min+=1
            if(self.min>59):
                self.min=0
                self.hour+=1
                if(self.hour>23):
                    self.hour=0

    def prev_second(self):
        self.sec -=1
        if(self.sec<0):
            self.sec = 59
            self.min-=1
            if(self.min<0):
                self.min=59
                self.hour-=1
                if(self.hour<0):
                    self.hour=23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
