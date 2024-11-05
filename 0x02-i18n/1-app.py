#!/usr/bin/env python3
"""using flask nd other dependecies"""
from flask import Flask,render_template
from flask_babel import Babel


app = Flask(__name__)


class config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
app.config.from_object(config)
babel = Babel(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

