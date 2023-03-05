from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager

url = "https://api.npoint.io/2378d3d8e0262f7e23d3"
posts = requests.get(url).json()

app = Flask(__name__)
notify = NotificationManager()

@app.route('/')
def home():
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
        
        notify.send_email(name, email, phone, message)
        return render_template("contact.html", success=True)
    elif request.method == "GET":
        return render_template("contact.html", success=False)
        


@app.route('/post/<int:id>')
def show_post(id):
    for post in posts:
        if post['id'] == id:
            return render_template("post.html", post=post)


""" @app.route('/form-entry', methods=['POST'])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"]) """
    


if __name__ == "__main__":
    app.run(debug=True)
