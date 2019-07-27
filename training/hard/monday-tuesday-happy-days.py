import sys
import math

def count_days(D, M):
    s = sum([ Month.by_ID[i].length for i in range(1, M)] )
    return s+D


class Month:
    instances = {}
    by_ID = {}
    def __init__(self, name, length, index):
        self.index = index
        self.name = name
        self.length = length
        self.instances[name] = self
        self.by_ID[index] = self
        self.number = len(list(self.instances.values()))
        #print('Created', self, file=sys.stderr)
        
    def __repr__(self):
        return 'Mois {} - {} - {} j'.format(self.number, self.name, self.length)


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


leap_year = int(input())
if leap_year == 1:
    d = 29
else:
    d = 28
    
Month('Jan', 31, 1)
Month('Feb',  d, 2)
Month('Mar', 31, 3)
Month('Apr', 30, 4)
Month('May', 31, 5)
Month('Jun', 30, 6)
Month('Jul', 31, 7)
Month('Aug', 31, 8)
Month('Sep', 30, 9)
Month('Oct', 31, 10)
Month('Nov', 30, 11)
Month('Dec', 31, 12)

source_day_of_week, source_month, source_day_of_month = input().split()

start_day = source_day_of_week
start_month = Month.instances[source_month].index
start_date = int(source_day_of_month)

print("start", start_day, start_date, start_month, file=sys.stderr)

target_month, target_day_of_month = input().split()

end_month = Month.instances[target_month].index
end_date = int(target_day_of_month)

print("end", end_date, end_month, file=sys.stderr)

number_of_day_1 = count_days(end_date, end_month)
number_of_day_2 = count_days(start_date, start_month)

print(number_of_day_2, number_of_day_1, file=sys.stderr)

shift = number_of_day_1-number_of_day_2

current_index = (days.index(source_day_of_week) + shift)%7
print(days[current_index])


