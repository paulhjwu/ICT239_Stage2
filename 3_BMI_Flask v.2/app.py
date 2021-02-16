import math
from flask import Flask,request,render_template,jsonify,url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index4.html')

@app.route('/process',methods= ['POST'])
def process():

  weight  = float(request.form['weight'])
  height = float(request.form['height'])

  if request.form['unit'] == 'm':
    bmi = weight / math.pow(height, 2)
  else:
    bmi = weight / math.pow(height/100, 2)

  return jsonify({'bmi' : bmi})

if __name__ == "__main__":
  app.run(debug=True)

  