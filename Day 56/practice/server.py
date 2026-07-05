from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


@app.route("/contact")
def contact():
    return render_template("contact-me.html")

if __name__ == '__main__':
    app.run(debug=True)