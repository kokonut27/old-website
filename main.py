from flask import Flask, render_template, flash, request, session, redirect, url_for, send_from_directory
import os
import json

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/projects')
def projects():
  return render_template("projects.html")

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.run(host="0.0.0.0", port=8080)