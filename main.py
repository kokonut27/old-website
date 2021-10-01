import json
import os
from flask import *

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

route = os.environ["secret"]

@app.route('/')
def index():
  return render_template(
    "index.html",
    page="Home")# make page differnt for every page, use base page and append from there.

@app.route('/about')
def about():
  return render_template(
    "about.html",
    page="About"
  )

@app.route('/projects')
def projects():
  return render_template(
    "projects.html",
    page="Projects"
  )

@app.route(f"/{route}")
def secret_page():
  return render_template(
    "")

@app.errorhandler(404)
def not_found(e):
  return render_template(
    "404.html",
    page="404 Error")

app.run(host="0.0.0.0", port=8080)