#!/usr/bin/env python3
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/marvel.html")
def marvel():
	return render_template("marvel.html")
#Dict des posters
posters = {"Iron Man":..., "The Incredible Hulk":..., "Iron Man 2":..., "Thor":..., "Captain America: The First Avenger":..., "Marvel's The Avengers":...,
              "Iron Man 3":..., "Thor: The Dark World":..., "Captain America: The Winter Soldier":..., "Guardians of the Galaxy":..., "Avengers: Age of Ultron":...,
              "Ant-Man":...,"Captain America : Civil War":..., "Doctor Strange":..., "Guardians of the Galaxy Vol. 2":..., "Spider-Man: Homecoming":...,
              "Thor: Ragnarok":..., "Black Panther":..., "Avengers: Infinity War":..., "Ant-Man and the Wasp":..., "Captain Marvel":..., "Avengers: Endgame":...,
              "Spider-Man: Far From Home":...,"Black Widow":..., "Shang-Chi and the Legend of the Ten Rings":..., "Eternals":..., "Spider-Man: No Way Home":...}

if __name__ == "__main__":
	app.run(host="localhost", port=80, debug=True)