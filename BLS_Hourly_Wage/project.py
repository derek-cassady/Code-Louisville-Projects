#Import libraries:
import requests
import json
#from prettytable import PrettyTable
import csv

#BLS series and data coding guide found at: 'https://www.bls.gov/developers/home.htm'
#A dictionary of HTTP headers to send to the specified url.

headers = {'Content-type': 'application/json'}

#Authentication key from BLS via 'https://data.bls.gov/registrationEngine/'

rkey = ("331efe7967c44039b40c36334f2014de")

#SeriesID formatting guide 'https://www.bls.gov/help/hlpforma.htm' for use in payload below:
    #Positions       Value           Field Name
	#1-2             CE              Prefix
	#3               U               Seasonal Adjustment Code
	#4-11		     08000000	     Supersector and Industry Codes
	#12-13           03              Data Type Code
    #CE - National Employment, Hours, and Earnings
    #U -  Not Seasonally Adjusted   
    #41423430 - Computer and software
    #08000000 - Total nonfarm
    #03	- AVERAGE HOURLY EARNINGS OF ALL EMPLOYEES
    #08 - AVERAGE HOURLY EARNINGS OF PRODUCTION AND NONSUPERVISORY EMPLOYEES
        #Series1 = CEU4142343003
        #Series2 = CEU4142343008
        #Series3 = CEU0800000003
        #Series4 = CEU0800000008
#payload = json.dumps({"seriesid":["Series1",..., "SeriesN"], "startyear":"YYYY", "endyear":"YYYY",
# "catalog":''default 'False'', "calculations":''default 'False'', "annualaverage":''default 'False'',"aspects":''default 'False'',
# "registrationkey":rkey}) 

payload = json.dumps({"seriesid":["CEU4142343003", "CEU4142343008", "CEU0800000003", "CEU0800000008"], "startyear":"2019", "endyear":"2022",
"catalog":False, "calculations":False, "annualaverage":False,"aspects":False,
"registrationkey":rkey}) 

#uses request library to post payload and headers to URL. Payload and headers specified variables above      
    #specified URL from BLS for JSON:'https://api.bls.gov/publicAPI/v2/timeseries/data/'
    #specified URL from BLS for Excel: 'https://api.bls.gov/publicAPI/v2/timeseries/data.xlsx'
#p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=payload, headers=headers)

f = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=payload, headers=headers)

#Saves requested JSON data from requests.post as variable 'json_data' to be modified by prettytable below

#data = json.load(f)

print(f.text)

#expected JSON response:
#"status": "REQUEST_SUCCEEDED",
#  "responseTime": 706,
#  "message": [ ],
#  "Results": [
# {
#       "series": [{
#        "seriesID": "WMU00140201020000001300002500",
#        "catalog": {
#          "series_title": "Average hourly wage for business and financial operations occupations, full-time, in Bloomington, IN",
#          "series_id": "WMU00140201020000001300002500",
#          "seasonality": "Not Seasonally Adjusted",
#          "survey_name": "Modeled Wage Estimates",
#          "survey_abbreviation": "WM",
#          "measure_data_type": "Average Hourly Wage",
#          "commerce_industry": "All industries",
#          "occupation": "Business and Financial Operations Occupations",
#          "occupation_work_class": "Civilian workers",
#          "area": "Bloomington, IN"
#        },
#        "data": [{
#          "year": "2018",
#          "period": "A01",
#          "periodName": "Annual",
#          "latest": "true",
#          "value": "30.71",
#          "aspects": [{
#            "name": "Relative Standard Error",
#            "value": "1.9",
#            "footnotes": [{}]
#          }],
#          "footnotes": [{}]

#directs to 'series' dictionary in 'json_data' 'Results' list of dictionaries
#begins "for loop":

for series in json_data['Results']['series']:

#Set variable 'X' for prettytables functions.
    #Additionally creates list of columns which will appear in row 0
    #'X' variable will be called and appended with '.add_row' later
#    x=PrettyTable(["series id","year","period","value","footnotes"])

    seriesId = series['seriesID']
    for item in series['data']:
#        year = item['year']
#        period = item['period']
#        value = item['value']
#        footnotes=""
#        for footnote in item['footnotes']:
#            if footnote:
#                footnotes = footnotes + footnote['text'] + ','
#checks for Month (MO1 - MO12) creates new row in pretty table for each Month found        
#        if 'M01' <= period <= 'M12':
#            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    
#Create variable 'output" will call variable and append later
#Variable 'seriesId' here SHOULD create new file for each series requested in 'Payload'
#create '.txt' file, named from 'json_data' list of dictionaries, allow write    

#    output = open(seriesId + '.txt','w')

#Calls variable 'output' and appends .write, calls variable 'x' for full string of data after '.add_row' completes  

#    output.write (x.get_string())

#appends 'output' variable to close file created above  

#    output.close()