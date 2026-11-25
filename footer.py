from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

@app.route("footer")
def home():
    current_year = date.today().year
    return render_template("index.html", year=current_year)