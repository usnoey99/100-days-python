from flask import Flask,render_template,redirect,url_for,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')
    if name:
        return redirect(url_for("guess", name=name))
    return render_template('index.html')

@app.route('/<name>')
def guess(name):
    response_gen = requests.get(f"https://api.genderize.io?name={name}")
    response_age = requests.get(f"https://api.agify.io?name={name}")
    gender = response_gen.json()["gender"]
    age = response_age.json()["age"]

    return render_template('guess.html', name=name, age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)