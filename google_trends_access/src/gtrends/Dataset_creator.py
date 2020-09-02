import sys
import csv
import pandas as pd
import numpy as np
import time
from gtrends_access import GTrendsAccessor
from datetime import datetime
from datetime import timedelta
from dateutil.rrule import rrule, WEEKLY





def make_one_call():
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'

    try:
                tf = sys.argv[3]
    except:
                tf = 'US'

    try:
                tf = sys.argv[3]
    except:
                tf = 'today 5-y'
            
    try:
                graph = sys.argv[4]
    except:
                graph = None
                
    df = GTrendsAccessor().api_result_with_graphics(kwd, state, time_range, graph)
    
    
            
def main():  #make this not main
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'
                
    try:
                tf = sys.argv[3]
    except:
                tf = '2018-06-29'
            

    
    date_list = list(rrule(WEEKLY, dtstart=datetime(2014,9,13), until=datetime(2014,9,27)))
    print("date",len(date_list))
    matrix = []
    for i in range(len(date_list)-1):
        start = date_list[i] + timedelta(days=1)
        start = start.strftime("%Y-%m-%d")
        end = date_list[i+1].strftime("%Y-%m-%d")
        time_range = start + " " + end
        
        states = states_list()
        index = 0
        for state in states:
            state = "US-"+state
            
            for i in range(len(date_list)-1):
                time.sleep(4)
                start = date_list[i].strftime("%Y-%m-%d")
                end = date_list[i+1].strftime("%Y-%m-%d")
                time_range = start + " " + end
                print(time_range)
                trend_values = GTrendsAccessor().api_result(kwd, state, time_range)
                trend_values = trend_values.tolist()
                trend_values.append(index)  #now trend_values has the values plus the region label at the end
                matrix.append(trend_values)
            time.sleep(170)
            index+=1
    
    file = open('dataset.csv', 'w+', newline ='')
    with file:
        write = csv.writer(file)
        write.writerows(matrix)
    


def states_list():
    with open('state.csv','r') as csv_file:
        lines = csv_file.readlines()

    number = []
    state_abbrev = []
    for line in lines:
        data = line.split(',')
        number.append(data[0])
        dat = data[1]
        state_abbrev.append(dat[:-1])
    return state_abbrev

    
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
