#!/bin/python
from datetime import date
import math

# arrive and depart visa dates
visas = []
visas.append((date(2015, 11, 2), date(2016, 4, 24)))
visas.append((date(2016, 7, 1), date(2016, 9, 27)))
visas.append((date(2016, 11, 24), date(2017, 3, 5)))
visas.append((date(2017, 11, 19), date(2018, 11, 16)))
visas.append((date(2018, 11, 17), date(2019, 12, 31)))
visas.append((date(2020, 1, 1), date.today()))

counter = 1
for visa in visas:
    print(f"visa{counter}: {(visa[1] - visa[0]).days} days, from {visa[0].strftime('%d/%m/%Y')} to {visa[1].strftime('%d/%m/%Y')}")
    counter = counter + 1
exit(0)