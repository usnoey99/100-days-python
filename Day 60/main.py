from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":

        data = request.form

        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]

        email_message = f"""
        Subject: New Message From Blog
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            # SMTP_SSL creates an encrypted connection automatically, so starttls() is not required.
            connection.login(user="MY_EMAIL@gmail.com", password="MY_PASSWORD")
            connection.sendmail(
                from_addr="MY_EMAIL",
                to_addrs="MY_EMAIL",
                msg=email_message
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
