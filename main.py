from flask import Flask, render_template
import requests

url = "https://api.npoint.io/2378d3d8e0262f7e23d3"
posts = requests.get(url).json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

""" @app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post) """

@app.route('/post/<int:id>')
def show_post(id):
    for post in posts:
        if post['id'] == id:
            print(post)
            return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
