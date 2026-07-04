from flask import Flask, render_template, request
import random

random_num = random.randint(0,99)
print(random_num)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess")
def guess_num():
    guess = int(request.args.get("guess"))

    if guess > random_num:
        return render_template(
            "result.html",
            color="purple",
            message="Too high!",
            gif="https://media1.giphy.com/media/Zu6AATBpCeUzm/giphy.gif"
        )

    elif guess < random_num:
        return render_template(
            "result.html",
            color="red",
            message="Too low!",
            gif="https://media2.giphy.com/media/Q3AMb3lxUkpmOS2TRq/giphy.gif"
        )

    else:
        return render_template(
            "result.html",
            color="green",
            message="You found me!",
            gif="https://media3.giphy.com/media/W1hd3uXRIbddu/giphy.gif"
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)