from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
import json,os

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/')
def index():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(host= "0.0.0.0", debug=True ,port=5000, threaded=True)
    # app.run(host= "0.0.0.0",port=5000, threaded=True)
