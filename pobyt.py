#!/bin/python
import datetime
import math

# arrive and depart visa dates
visa1 = (datetime.datetime(2015, 11, 2), datetime.datetime(2016, 4, 24))
visa2_arrive = datetime.datetime(2016, 7, 1)
visa2_depart = datetime.datetime(2016, 9, 27)
visa3_arrive = datetime.datetime(2016, 11, 24)
visa3_depart = datetime.datetime(2017, 3, 5)
visa4_arrive = datetime.datetime(2017, 11, 19)
visa4_depart = datetime.datetime(2018, 11, 16)
pobyt1_start = datetime.datetime(2018, 11, 17) # 2018-11-30 official date
pobyt1_end = datetime.datetime(2019, 12, 31)
pobyt2_start = datetime.datetime(2019, 4, 17) # 2018-11-30 official date
pobyt2_end = datetime.datetime.now()

ranges = []
#ranges.append((visa1_depart - visa1_arrive).days)
#ranges.append((visa2_depart - visa2_arrive).days)
#ranges.append((visa3_depart - visa3_arrive).days)
ranges.append((visa4_depart - visa4_arrive).days)
ranges.append((pobyt_end - pobyt_start).days)

total = (pobyt_end - visa1_arrive).days
total_spended = 0

for element in ranges:
                     total_spended = total_spended + element

missed = (pobyt_end - visa1_arrive).days - total_spended
print("total spended days: {0} (or {1} years and {2} days)".format(total_spended, total_spended / 365, total_spended % 365))
print("total: {0} (or {1} years and {2} days)".format(total, total / 365, total % 365))
print("I missed {0} days".format(missed))

break_max_allowed = 6 * 31
break_total = 10 * 31

if missed > break_total:
                     print("you exceeded a limit of total break ({0})".format(break_total))

miss1 = abs((visa1_depart - visa2_arrive).days)
miss2 = abs((visa2_depart - visa3_arrive).days)
miss3 = abs((visa3_depart - visa4_arrive).days)
miss4 = abs((visa4_depart - pobyt_start).days)
print("max allowed break: {0}".format(break_max_allowed))
print(miss1)
print(miss2)
print(miss3)
print(miss4)

pobyt_staty = 5 * 365
print("pozostalo: {0}".format((pobyt_staty - total_spended) / 365))