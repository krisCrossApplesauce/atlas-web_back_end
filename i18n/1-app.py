#!/usr/bin/env python3
""" setup a basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ to configure available languages in the app """
    LANGUAGES = ["en", "fr"]

    def get_locale(cls):
        """ returns language """
        return request.accept_languages.best_match(cls.LANGUAGES)

    def get_timezone(cls):
        """ returns timezone """
        return "UTC"


app = Flask(__name__)
babel = Babel(app, locale_selector=Config.get_locale, timezone_selector=Config.get_timezone)


@app.route('/')
def hello_world():
    """ returns the index.html template """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
