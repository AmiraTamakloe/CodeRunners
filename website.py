#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/marvel.html")
def marvel():
	return render_template("marvel.html")

if __name__ == "__main__":
	app.run(host="localhost", port=80, debug=True)