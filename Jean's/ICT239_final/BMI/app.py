from flask import Flask, request, render_template, jsonify
import math

from datetime import datetime, timedelta 
import csv

#connect to MongoDB

import pymongo
#connect to the default local server database
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['bmi']

app = Flask(__name__)

def csv_to_dict(file):
    
    with file as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = csv.DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        list_of_dict = list(dict_reader)
        # print list of dict i.e. rows
        file.close()
        return list_of_dict

def storeReadings(data, db):
    
    readings = {}
    fDate = datetime(3000, 1, 1)
    lDate = datetime(2000, 12, 31)

    for item in data:

        parts = [int(x) for x in item['Date'].split('-')]
        myDate = datetime(parts[0], parts[1], parts[2])

        if myDate <= fDate:
            fDate = myDate

        if myDate >= lDate:
            lDate = myDate
        
        if readings.get(item['User']):
            readings[item['User']].append([item['Date'], item['BMI']])            
        else:
            readings[item['User']] = [[item['Date'], item['BMI']]]

    db.readings.insert_one({"readings": readings, "fDate": fDate, "lDate": lDate})

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

# '/' path - refer to the main path = index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load')
def load():
    # return render_template('BMI_Chart.html')
    f1 = open("static/DataSet2.csv", "r")
    listOfDict = csv_to_dict(f1)
    storeReadings(listOfDict, db)
    return render_template('loaded.html')

@app.route('/chart')
def chart():
    # return render_template('BMI_Chart.html')
    return render_template('BMI_Chart.html')

@app.route('/chart2', methods=['GET', 'POST'])
def chart2():
    # return render_template('BMI_Chart.html')
    if request.method == 'GET':
            #I want to get some data from the service
        return render_template('BMI_Chart2.html')    #do nothing but to show index.html

    elif request.method == 'POST':

        #Get the values passed from the Front-end, do the BMI calculation, return the BMI back to front-end
        # f1 = open("static/DataSet2.csv", "r")
        #listOfDict = csv_to_dict(f1)

        dbCursor = db.readings.find({})

        readings = {}
        fDate = datetime.now()
        lDate = datetime.now()

        #readings, bDate, lDate = getReadings(listOfDict)
        readings = dbCursor[0]["readings"]
        fDate = dbCursor[0]["fDate"]
        lDate = dbCursor[0]["lDate"]

        chartDim = {}
        labels = []

        chartDim, labels = dataPrep(readings, fDate, lDate)

        #print(chartDim, labels)

        return jsonify({'chartDim': chartDim, 'labels': labels})

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

@app.route('/chart3', methods=['GET', 'POST'])
def chart3():
    # return render_template('BMI_Chart.html')
    if request.method == 'GET':
            #I want to get some data from the service
        return render_template('BMI_Chart3.html')    #do nothing but to show index.html

    elif request.method == 'POST':

        #Get the values passed from the Front-end, do the BMI calculation, return the BMI back to front-end
        # f1 = open("static/DataSet2.csv", "r")
        #listOfDict = csv_to_dict(f1)

        db2 = connection['bmi']
        aveDict = getAverage(db2)

        return jsonify({'averages': aveDict})

@app.route('/process',methods= ['POST'])
def process():

    weight  = float(request.form['weight'])
    height = float(request.form['height'])

    if request.form['unit'] == 'm':
        bmi = weight / math.pow(height, 2)
    else:
        bmi = weight / math.pow(height/100, 2)

    return jsonify({'bmi' : bmi})

# @app.route('/process', methods=['GET', 'POST'])
# def process():

#     if request.method == 'GET':
#         #I want to get some data from the service
#         return render_template('index.html')    #do nothing but to show index.html

#     elif request.method == 'POST':
#         #Get the values passed from the Front-end, do the BMI calculation, return the BMI back to front-end

#         weight = float(request.form['weight'])
#         height = float(request.form['height'])
#         unit = request.form['unit']

#         if unit == 'm':
#             bmi = weight / math.pow(height, 2)

#         else:
#             bmi = weight / math.pow(height/100, 2)

#         print(f'The BMI is {bmi}')

#         return jsonify({'bmi': bmi})

# app.run(debug=True, host='0.0.0.0')

if __name__ == "__main__":
  app.run(debug=True)