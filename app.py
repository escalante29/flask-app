from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/about")
def about():
    return "<h2>About this app...</h2>"


@app.route("/stocks/")
def stocks():
    return "<h2>Stocks list...</h2>"


@app.route("/hello/<message>")
def hello_message(message):
    return f"<h1>Welcome {escape(message)}!</h1>"


@app.route("/blog_posts/<post_id>")
def display_blog_post(post_id):
    return f"<h1>Blog Post #{post_id}...</h1>"
