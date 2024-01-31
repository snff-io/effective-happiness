
from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})



@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


