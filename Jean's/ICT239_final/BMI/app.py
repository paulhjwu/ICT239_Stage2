from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

# '/' path - refer to the main path = index.html
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart')
def chart():
    return render_template('BMI_Chart.html')

@app.route('/process', methods=['GET', 'POST'])
def process():

    if request.method == 'GET':
        #I want to get some data from the service
        return render_template('index.html')    #do nothing but to show index.html

    elif request.method == 'POST':
        #Get the values passed from the Front-end, do the BMI calculation, return the BMI back to front-end

        weight = float(request.form['weight'])
        height = float(request.form['height'])
        unit = request.form['unit']

        if unit == 'm':
            bmi = weight / math.pow(height, 2)

        else:
            bmi = weight / math.pow(height/100, 2)

        print(f'The BMI is {bmi}')

        return jsonify({'bmi': bmi})


app.run(debug=True, host='0.0.0.0')