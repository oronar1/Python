from flask import Flask, render_template
import requests
from datetime import date

BLOG_POSTS = requests.get(url='https://api.npoint.io/eb6cd8a5d783f501ee7d').json()

app = Flask(__name__)


@app.route('/post/<int:id_num>')
def get_post(id_num):
    post = BLOG_POSTS[id_num-1]
    return render_template("post.html", post=post,image=post['image_url'])

@app.route('/about.html')
def about():
    year = date.today().year
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    year = date.today().year
    return render_template("contact.html")

@app.route('/')
@app.route('/index.html')
def home():
    # year = date.today().year
    return render_template("index.html", posts=BLOG_POSTS)

if __name__ == "__main__":
    app.run(debug=True)
