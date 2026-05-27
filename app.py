from flask import Flask, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Proxy is running!"
