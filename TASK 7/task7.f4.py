class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        
    def addTime(time1, time2):
        minutes = time1.minutes + time2.minutes
        hours = time1.hours + time2.hours
        if minutes >= 60:
            hours += 1
            minutes = minutes % 60
        return Time(hours, minutes)
    
    def displayTime(self):
        print("{} hour(s) and {} minute(s)".format(self.hours, self.minutes))
        
    def displayMinutes(self):
        total_minutes = self.hours * 60 + self.minutes
        print("Total minutes: {}".format(total_minutes))
time1 = Time(2, 50)
time2 = Time(1, 20)
time3 = Time.addTime(time1, time2)

time3.displayTime()


time3.displayMinutes()

