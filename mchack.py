from flask import Flask, redirect, session, url_for, render_template, request, session, flash
from datetime import timedelta
from mcu import recommandation
app = Flask(__name__)
app.secret_key = "password"
app.permanent_session_lifetime = timedelta(hours=5)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    film = recommandation(request.form['variable'])
    
    return render_template("movie.html", content=film)
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/movie")
def movie():
    return render_template("movie.html")


if __name__ == "__main__":
    app.run(debug=True)
    
