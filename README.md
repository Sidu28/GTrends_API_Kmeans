## Introduction
This program allows us to process google search trend data for a particualr search term and analyze it using k-means clustering.  Additionally, it provides visualization using Principle component analysis to reduce the dimensionality to 2.  This allows us to see the clusters form in 2-space.  It includes a method that allows us to make calls to the Google Trends API.


## Making Calls to the Google Trend API

```bash
cd google_trends_access
```
Once you are there, run the following command:
```bash
python src/gtrends/gtrends_access.py keyword region timeframe graph
```
Here the keyword is the google search term you want to retrieve data for.  The region is the region of interest that you want to select.  The format of the region parameter is based on the [UNECE Codes for Trade](http://www.unece.org/cefact/codesfortrade/codes_index.html).  In order to look up the region code that you require, please take a look at the countries.rda file.  Include the parameter 'graph' to generate a plot of the data.  For the time frame parameter, there are a few formatting options:

**Timeframe**

* Date to start from

* Defaults to last 5yrs, 'today 5-y'.

* Everything 'all'

* Specific dates, 'YYYY-MM-DD YYYY-MM-DD' example '2016-12-14 2017-01-25'

* Specific datetimes, 'YYYY-MM-DDTHH YYYY-MM-DDTHH' example '2017-02-06T10 2017-02-12T07'

   * Note Time component is based off UTC
* Current Time Minus Time Pattern:

    * By Month: 'today #-m' where # is the number of months from that date to pull data for

        * For example: 'today 3-m' would get data from today to 3months ago
        * NOTE Google uses UTC date as 'today'
        * Seems to only work for 1, 2, 3 months only
    * Daily: 'now #-d' where # is the number of days from that date to pull data for
        * For example: 'now 7-d' would get data from the last week
        * Seems to only work for 1, 7 days only
    * Hourly: 'now #-H' where # is the number of hours from that date to pull data for

        * For example: 'now 1-H' would get data from the last hour
        * Seems to only work for 1, 4 hours only


## Input Format
 The input to this program is a CSV file formatted as follows.  Each entry is made up of the google search trend values for a particualr search term for a given location, over a set time period.  In addition, each entry is labelled based on the state it is from (Where numbers 1 to 50 refer to states in alphabetical order).  These labels allow us to compare our clustering to the actual location of states.  

1 | 2 | 3 | labels
------------ | ------------- | ------------- | -------------
2 | 100 | 44 | 2
13 | 100 | 21 | 10
5 | 90 | 44 | 4

To run the program, run the following command: 
```bash
python3 kmeans.py filename.csv
```
