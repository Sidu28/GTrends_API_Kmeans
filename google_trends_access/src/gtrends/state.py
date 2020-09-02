import sys
import csv
import pandas as pd
import numpy as np
from gtrends_access import GTrendsAccessor
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY


with open('states.csv','r') as csv_file:
    lines = csv_file.readlines()

number = []
state_abbrev = []
for line in lines:
    data = line.split(',')
    number.append(data[0])
    state_abbrev.append(data[1])
print(state_abbrev)
