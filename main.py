import json
from flask import *

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/')
def index():
  return render_template("index.html")