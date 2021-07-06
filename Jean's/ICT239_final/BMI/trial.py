import csv
from datetime import datetime, timedelta
import io
import pandas as pd
import numpy as np

import pymongo
import math

# To run mongod in Windows: mongod --dbpath ~/data &
# Configure MongoDB

connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['catalog']

def create_recording(aType, _datetime, count):
    assert aType is not None
    assert _datetime is not None
    assert count is not None

    db.recordings.insert_one({
        "type": aType,
        "datetime": _datetime,
        "count": count,
    })

def upload_recording_to_df(file):
    assert file is not None

    #data = file.read()
    df1 = pd.read_csv(file, header=0, encoding = "utf-8")
    aList = []

    for index, row in df1.iterrows():
        aList.append([row["Id"], row["created_at"], row['Type'], 1])

    df2 = pd.DataFrame(aList, columns=['id', 'created_at', 'type', 'count'])

    df2["created_at"] = pd.to_datetime(df2["created_at"])
    df2["Date_received_year"] = pd.DatetimeIndex(df2["created_at"]).year
    df2["Date_received_qtr"] = df2["created_at"].dt.quarter
    df2["Date_received_year_qtr"] = df2["Date_received_year"].astype(str) + ' Q' +  df2["Date_received_qtr"].astype(str) 

    df3 = pd.pivot_table(df2, values="count", index=["Date_received_year_qtr"], columns=["type"], aggfunc=np.sum)
    
    return df3

def csv_to_dict(file):

    with file as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = csv.DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        # print list of dict i.e. rows
        return (list_of_dict)

def upload_recording_to_mongodb(file, db):

    assert file is not None

    dictList = csv_to_dict(file)
    for aDict in dictList:
        aDict["created_at"] = datetime.strptime(aDict['created_at'], "%a %b %d %H:%M:%S %z %Y")
        aDict["Date_received_year"] = aDict["created_at"].year
        aDict['Date_received_qtr'] = math.ceil(aDict["created_at"].month/3)
        aDict['Date_received_year_qtr'] = str(aDict["Date_received_year"]) + "-" + str(aDict["Date_received_qtr"])
        db.recordings.insert_one(aDict)

#f1 = open("static/sample.csv", "r")
#f2 = open("static/countByQuarter.csv", "w")

# // Using Pandas
#df2 = upload_recording_to_df(f1)
# print(df2.index.to_list())
# print(df2.columns.to_list())
# df2['text'] = df2['text'].fillna(0)
# print(df2['text'].to_list())

# // Using MongoDB

#upload_recording_to_mongodb(f1, db)

def pivotCount(db):

    results = db.recordings.aggregate(
        [
            # count occurence
            # https://stackoverflow.com/questions/27177836/how-to-count-all-occurrences-of-an-element-in-mongodb 

            {"$group":{"_id":"$Type","count":{"$sum": 1}}},
            #{"$project":{"Type":"$_id","occurance":"$count"}}
            {"$project":{"count": 1}}

        ]
    )

    return results

# results = pivotCount(db)

# for record in results:
#     print(record)

f1 = open("static/DataSet2.csv", "r")
#f2 = open("static/DataSet3.csv", "w")

# def rePopulate(f1, f2):

#     dictList = csv_to_dict(file)

#     for aDict in dictList:
#             aDict["created_at"] = datetime.strptime(aDict['created_at'], "%a %b %d %H:%M:%S %z %Y")
#             aDict["Date_received_year"] = aDict["created_at"].year
#             aDict['Date_received_qtr'] = math.ceil(aDict["created_at"].month/3)
#             aDict['Date_received_year_qtr'] = str(aDict["Date_received_year"]) + "-" + str(aDict["Date_received_qtr"])
#             db.recordings.insert_one(aDict)


data = csv_to_dict(f1)

readings={}
bDate = datetime(3000, 1, 1)
lDate = datetime(2000, 12, 31)

def getReadings(data):

    readings = {}
    bDate = datetime(3000, 1, 1)
    lDate = datetime(2000, 12, 31)

    for item in data:

        parts = [int(x) for x in item['Date'].split('-')]
        myDate = datetime(parts[0], parts[1], parts[2])

        if myDate <= bDate:
            bDate = myDate

        if myDate >= lDate:
            lDate = myDate
        
        if readings.get(item['User']):
            readings[item['User']].append([item['Date'], item['BMI']])            
        else:
            readings[item['User']] = [[item['Date'], item['BMI']]]

    return readings, bDate, lDate

def dataPrep(readings, bDate, lDate):

    chartDim = {}
    labels = []

    start_date = bDate
    end_date = lDate
    delta = timedelta(days=1)

    while start_date <= end_date:

        month = str(start_date.month) # months from 1-12
        day = str(start_date.day)
        year = str(start_date.year)

        aDateString = year + "-" + month + "-" + day
        labels.append(aDateString);

        for key, values in readings.items():

            if not chartDim.get(key):
                chartDim[key]=[];   
          
            filled = False

            for item in values:

                parts=[ int(x) for x in item[0].split('-') ]
                mydate = datetime(parts[0], parts[1], parts[2]) 
                
                if mydate == start_date:
                    
                    chartDim[key].append(item[1])
                    filled = True

                else:

                    if mydate > start_date:
                        if not filled:
                            chartDim[key].append(-1)
                        break

        start_date += delta

    return chartDim, labels

#readings, bDate, lDate = getReadings(data)

#print(readings, bDate, lDate)

#chartDim, labels = dataPrep(readings, bDate, lDate)

#print(chartDim, labels)

db2 = connection['bmi']

def getAverage(db):

    aveDict = {}
    sum=0
    count=0
    resCursor = db.readings.find({})  
    readings = resCursor[0]["readings"]
    
    for key, values in readings.items():

        for value in values:
            sum += float(value[1])
            count += 1
        
        aveDict[key]=sum/count
    
    return aveDict

aveDict = getAverage(db2)
print(aveDict)

