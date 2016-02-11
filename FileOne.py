import sys

print(sys.version_info)


def calculate_date_100(your_age):
    time_till_100 = 100 - your_age
    hundred_date = 2016 + time_till_100
    return hundred_date

name = raw_input("Enter your name: ")
current_age = raw_input("Enter your age: ")
date = calculate_date_100(int(current_age))
print "Hello %s, you will turn 100 in the year %s" % (str(name), date)
