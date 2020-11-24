#!/bin/python
from datetime import date as d
import math

# arrive and depart visa dates
visas = []
add = visas.append
add((d(2015, 11, 2), d(2016, 4, 24)))
add((d(2016, 7, 1), d(2016, 9, 27)))
add((d(2016, 11, 24), d(2017, 3, 5)))
add((d(2017, 11, 19), d(2018, 11, 16)))
add((d(2018, 11, 17), d(2019, 12, 31)))
add((d(2020, 1, 1), d.today()))

counter = 1
for visa in visas:
    print(f"visa{counter}: {(visa[1] - visa[0]).days} days, from {visa[0].strftime('%d/%m/%Y')} to {visa[1].strftime('%d/%m/%Y')}")
    counter = counter + 1
exit(0)