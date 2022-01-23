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
posters = {"Iron Man":"{{url_for('static', filename='styles/style.css')}}", "The Incredible Hulk":"{{url_for('static', filename='styles/style.css')}}", "Iron Man 2":"{{url_for('static', filename='styles/style.css')}}", "Thor":"{{url_for('static', filename='styles/style.css')}}", "Captain America: The First Avenger":"{{url_for('static', filename='styles/style.css')}}", "Marvel's The Avengers":"{{url_for('static', filename='styles/style.css')}}",
              "Iron Man 3":"{{url_for('static', filename='styles/style.css')}}", "Thor: The Dark World":"{{url_for('static', filename='styles/style.css')}}", "Captain America: The Winter Soldier":"{{url_for('static', filename='styles/style.css')}}", "Guardians of the Galaxy":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Age of Ultron":"{{url_for('static', filename='styles/style.css')}}",
              "Ant-Man":"{{url_for('static', filename='styles/style.css')}}","Captain America : Civil War":"{{url_for('static', filename='styles/style.css')}}", "Doctor Strange":"{{url_for('static', filename='styles/style.css')}}", "Guardians of the Galaxy Vol. 2":"{{url_for('static', filename='styles/style.css')}}", "Spider-Man: Homecoming":"{{url_for('static', filename='styles/style.css')}}",
              "Thor: Ragnarok":"{{url_for('static', filename='styles/style.css')}}", "Black Panther":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Infinity War":"{{url_for('static', filename='styles/style.css')}}", "Ant-Man and the Wasp":"{{url_for('static', filename='styles/style.css')}}", "Captain Marvel":"{{url_for('static', filename='styles/style.css')}}", "Avengers: Endgame":"{{url_for('static', filename='styles/style.css')}}",
              "Spider-Man: Far From Home":"{{url_for('static', filename='styles/style.css')}}","Black Widow":"{{url_for('static', filename='styles/style.css')}}", "Shang-Chi and the Legend of the Ten Rings":"{{url_for('static', filename='styles/style.css')}}", "Eternals":"{{url_for('static', filename='styles/style.css')}}", "Spider-Man: No Way Home":"{{url_for('static', filename='styles/style.css')}}"}

if __name__ == "__main__":
	app.run(host="localhost", port=80, debug=True)