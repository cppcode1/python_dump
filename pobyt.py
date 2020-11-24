#!/bin/python
import datetime
import math

# arrive and depart visa dates
visas = []
visas.append((datetime.date(2015, 11, 2), datetime.date(2016, 4, 24)))
visas.append((datetime.date(2016, 7, 1), datetime.date(2016, 9, 27)))
visas.append((datetime.date(2016, 11, 24), datetime.date(2017, 3, 5)))
visas.append((datetime.date(2017, 11, 19), datetime.date(2018, 11, 16)))
visas.append((datetime.date(2018, 11, 17), datetime.date(2019, 12, 31)))
visas.append((datetime.date(2020, 1, 1), datetime.date.today()))

counter = 1
for visa in visas:
    print(f"visa{counter}: {(visa[1] - visa[0]).days} days, from {visa[0].strftime('%d/%m/%Y')} to {visa[1].strftime('%d/%m/%Y')}")
    counter = counter + 1
exit(0)