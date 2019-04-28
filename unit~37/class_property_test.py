class Date:
    @classmethod
    def is_date_valid(cls, dateStr):
        if int(dateStr[5:7]) >= 1 and int(dateStr[5:7]) <= 12 and int(dateStr[8:10]) >= 1 and int(dateStr[8:10]) <= 31:
            return True
        else:
            return False

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
 
    @classmethod
    def is_time_valid(cls, time_string):
        hour_tmp, min_tmp, sec_tmp = map(int, time_string.split(':'))
        if hour_tmp <= 24 and min_tmp <= 59 and sec_tmp <= 60:
            return True
        else:
            return False
    
    @classmethod
    def from_string(cls, time_string):
        hour_tmp, min_tmp, sec_tmp = map(int, time_string.split(':'))
        t = Time(hour_tmp, min_tmp, sec_tmp)
        return t

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')