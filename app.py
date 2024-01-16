from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Uses handler for /home."""

    return home_page()


@app.route("/home")
def home_page():
    """Return homepage."""

    return render_template("home.html", word_types=story.prompts)


@app.route("/story", methods=["POST"])
def story_page():
    """Return story."""

    return render_template("story.html", story_text=story.generate(request.form))
