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

    return render_template("home.html", stories_length=len(stories), stories=stories)


@app.route("/story/prompt")
def story_prompt():
    """Returns a page that prompts the user for the words to use in a Mad Libs story."""

    story_id = int(request.args["story-id"])

    return render_template("prompt.html", story_id=story_id, word_types=stories[story_id].prompts)


@app.route("/story/<int:story_id>/result", methods=["POST"])
def story_page(story_id):
    """Return story."""

    return render_template("story.html", story_text=stories[story_id].generate(request.form))
