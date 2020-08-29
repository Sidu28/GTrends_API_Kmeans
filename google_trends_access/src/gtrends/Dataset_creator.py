import sys
import csv
import pandas as pd
import numpy as np
from gtrends_access import GTrendsAccessor
from datetime import datetime
from dateutil.rrule import rrule, WEEKLY

states = ["US-AL", "US-AK", "US-AZ"]



def main():
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'
            
    try:
                region = sys.argv[2]
    except:
                region = None
                
    try:
                tf = sys.argv[3]
    except:
                tf = 'today 5-y'
            
    try:
                graph = sys.argv[4]
    except:
                graph = None
                    
    date_list = list(rrule(WEEKLY, dtstart=datetime(2014,12,13), until=datetime(2014,12,25)))
    matrix = []
    for i in range(len(date_list)-1):
        start = date_list[i].strftime("%Y-%m-%d")
        end = date_list[i+1].strftime("%Y-%m-%d")
        time_range = start + " " + end
        
        for state in states:
            trend_values = GTrendsAccessor().api_result(kwd, state, time_range, None)
            trend_values = trend_values.tolist()
            trend_values.append(state)  #now trend_values has the values plus the region label at the end
            matrix.append(trend_values)
    
    file = open('dataset.csv', 'w+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(matrix)
    

    
    
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
