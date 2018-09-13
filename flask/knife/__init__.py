from flask import Flask
from flask import render_template
from flask_mongoengine import MongoEngine
from flask_mongoengine import MongoEngineSessionInterface

app = Flask(__name__)

app.config.from_object("knife.config.EnvConfig")

engine = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(engine)

@app.route("/")
def index():
    return "test"
