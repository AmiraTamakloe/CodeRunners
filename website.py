#!/usr/bin/env python3
from flask import Flask, redirect, session, url_for, render_template, request, session, flash
from datetime import timedelta
from mcu import recommandation

app = Flask(__name__)
app.secret_key = "password"
app.permanent_session_lifetime = timedelta(hours=5)


@app.route('/moviesearch.html', methods=['POST'])
def my_form_post():
	film = recommandation(request.form['variable'])
	
	return render_template("movie.html", movie1=film[1], movie2=film[2], movie3=film[3])
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/marvel.html")
def marvel():
	return render_template("marvel.html")

@app.route("/moviesearch.html")
def moviesearch():
	return render_template("moviesearch.html")

if __name__ == "__main__":
	app.run(debug=True)