from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
  return os.environ["FLASK_ENV"]
