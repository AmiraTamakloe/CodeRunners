#!/usr/bin/env python3
from flask import Flask, redirect, session, url_for, render_template, request, session, flash
from datetime import timedelta
from mcu import recommandation

#Dict des posters
posters = {"Iron Man":"static/img/iron1.jpg", "The Incredible Hulk":"static/img/hulk.jpg", "Iron Man 2":"static/img/ironman2.jpg", "Thor":"static/img/thor.jpg", "Captain America: The First Avenger":"static/img/cap1staven.jpg", "Marvel's The Avengers":"static/img/avengers.jpg",
              "Iron Man 3":"static/img/ironman3.jpeg", "Thor: The Dark World":"static/img/thordarkworld.jpg", "Captain America: The Winter Soldier":"static/img/capwinter.jpg", "Guardians of the Galaxy":"static/img/guardians.jpeg", "Avengers: Age of Ultron":"static/img/ultron.jpg",
              "Ant-Man":"static/img/ant.jpeg","Captain America : Civil War":"static/img/civilwar.webp", "Doctor Strange":"static/img/docstrange.jpg", "Guardians of the Galaxy Vol. 2":"static/img/guardians2.webp", "Spider-Man: Homecoming":"static/img/homecoming.jpeg",
              "Thor: Ragnarok":"static/img/ragnarok.jpg", "Black Panther":"static/img/blackpanther.jpg", "Avengers: Infinity War":"static/img/infinity.jpg", "Ant-Man and the Wasp":"static/img/wasp.jpg", "Captain Marvel":"static/img/capmarvel.jpg", "Avengers: Endgame":"static/img/aven.jpeg",
              "Spider-Man: Far From Home":"static/img/farfromhome.jpg","Black Widow":"static/img/black.jpeg", "Shang-Chi and the Legend of the Ten Rings":"static/img/shang.jpeg", "Eternals":"static/img/eternals.jpg", "Spider-Man: No Way Home":"static/img/spiderman3.jpeg"}

app = Flask(__name__)
#app.secret_key = "password"
#app.permanent_session_lifetime = timedelta(hours=5)


@app.route('/moviesearch.html', methods=['POST'])
def my_form_post():
	film = recommandation(request.form['variable'])
	print("#########################################################", posters[film[1]])
	return render_template("movie.html", movie1=film[1], movie2=film[2], movie3=film[3], poster1 = posters[film[1]], poster2 = posters[film[2]], poster3 = posters[film[3]])
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