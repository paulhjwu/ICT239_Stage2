from flask import Flask

#__name__ means this current file
app = Flask(__name__)

#Route the website to a default page
@app.route('/')
def home():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)



