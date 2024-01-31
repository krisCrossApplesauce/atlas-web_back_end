#!/usr/bin/env python3
""" setup a basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    """ ok now I make a get_locale func """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config():
    """ to configure language and timezone in the app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """ returns the index.html template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
