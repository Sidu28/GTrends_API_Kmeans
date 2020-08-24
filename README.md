## Introduction
This program allows us to process google search trend data for a particualr search term and analyze it using k-means clustering.  Additionally, it provides visualization using Principle component analysis to reduce the dimensionality to 2.  This allows us to see the clusters form in 2-space.  

## Input Format
 The input to this program is a CSV file formatted as follows.  Each entry is made up of the google search trend values for a particualr search term for a given location, over a set time period.  In addition, each entry is labelled based on the state it is from (Where numbers 1 to 50 refer to states in alphabetical order).  These labels allow us to compare our clustering to the actual location of states.  

1 | 2 | 3 | labels
------------ | ------------- | ------------- | -------------
2 | 100 | 44 | 2
13 | 100 | 21 | 10
5 | 90 | 44 | 4

To run the program, run the following command: 
```bash
python3 data.py filename.csv
```
