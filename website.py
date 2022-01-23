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
#Dict des posters
posters = {"Iron Man":"{{url_for('static', filename='styles/style.css')}}", "The Incredible Hulk":"{{url_for('static', filename='styles/style.css')}}", "Iron Man 2":"{{url_for('static', filename='styles/style.css')}}", "Thor":"{{url_for('static', filename='styles/style.css')}}", "Captain America: The First Avenger":"{{url_for('static', filename='styles/style.css')}}", "Marvel's The Avengers":"{{url_for('static', filename='styles/style.css')}}",
              "Iron Man 3":"{{url_for('static', filename='styles/style.css')}}", "Thor: The Dark World":"{{url_for('static', filename='styles/style.css')}}", "Captain America: The Winter Soldier":"{{url_for('static', filename='styles/style.css')}}", "Guardians of the Galaxy":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Age of Ultron":"{{url_for('static', filename='styles/style.css')}}",
              "Ant-Man":"{{url_for('static', filename='styles/style.css')}}","Captain America : Civil War":"{{url_for('static', filename='styles/style.css')}}", "Doctor Strange":"{{url_for('static', filename='styles/style.css')}}", "Guardians of the Galaxy Vol. 2":"{{url_for('static', filename='styles/style.css')}}", "Spider-Man: Homecoming":"{{url_for('static', filename='styles/style.css')}}",
              "Thor: Ragnarok":"{{url_for('static', filename='styles/style.css')}}", "Black Panther":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Infinity War":"{{url_for('static', filename='styles/style.css')}}", "Ant-Man and the Wasp":"{{url_for('static', filename='styles/style.css')}}", "Captain Marvel":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Endgame":"{{url_for('static', filename='styles/style.css')}}",
              "Spider-Man: Far From Home":"{{url_for('static', filename='styles/style.css')}}","Black Widow":"{{url_for('static', filename='styles/style.css')}}", "Shang-Chi and the Legend of the Ten Rings":"{{url_for('static', filename='styles/style.css')}}", "Eternals":"{{url_for('static', filename='styles/style.css')}}", "Spider-Man: No Way Home":"{{url_for('static', filename='styles/style.css')}}"}

@app.route("/moviesearch.html")
def moviesearch():
	return render_template("moviesearch.html")

if __name__ == "__main__":
	app.run(debug=True)