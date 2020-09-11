import sys
import csv
import argparse
import pandas as pd
import numpy as np
import time
from gtrends_access import GTrendsAccessor
from datetime import datetime
from datetime import timedelta
from dateutil.rrule import rrule, WEEKLY
from sklearn import manifold



def main():

    choice = input("Would you like to run one call or compile multiple calls (answer: one/mult):  ")
    
    if choice == 'once':
        single_call()
    
    if choice == 'mult':
        mult_call()
        
        
def single_call():
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'

    try:
                 state = sys.argv[3]
    except:
                state = 'US'

    try:
                tf = sys.argv[3]
    except:
                tf = 'today 5-y'
            
    try:
                graph = sys.argv[4]
    except:
                graph = None
                
    df = GTrendsAccessor().api_result_with_graphics(kwd, state, tf, graph)
    
    
            
def mult_call():  #make this not main
    try:
                kwd = sys.argv[1]
    except:
                kwd = 'Vote'
                
    try:
                tf1 = sys.argv[2]
    except:
                tf1 = '2018-06-29'
    try:
                tf2 = sys.argv[3]
    except:
                tf2 = '2018-06-30'
            

    start = datetime.strptime(tf1, '%Y-%m-%d')
    end = datetime.strptime(tf2, '%Y-%m-%d')
    date_list = list(rrule(WEEKLY, dtstart=start, until=end))
    print("date",len(date_list))
    matrix = []

    states = states_list()
    index = 0
    for state in states:
        state = "US-"+state
            
        for i in range(len(date_list)-1):
            time.sleep(3)
            date = date_list[i] + timedelta(days=1)
            start = date.strftime("%Y-%m-%d")
            end = date_list[i+1].strftime("%Y-%m-%d")
            time_range = start + " " + end
            print(time_range)
            trend_values = GTrendsAccessor().api_result(kwd, state, time_range)
            trend_values = trend_values.tolist()
            trend_values.append(index)  #now trend_values has the values plus the region label at the end
            matrix.append(trend_values)
        time.sleep(10)
        index+=1
    
     
    curr_moment = time.strftime("%Y-%b-%d__%H:%M:%S",time.localtime())
    file = open('dataset_'+tf1[0:3]+'_'+kwd+'.csv', 'w+', newline ='')
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
