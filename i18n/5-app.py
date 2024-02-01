#!/usr/bin/env python3
""" setup a basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ to configure language and timezone in the app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ ok now I make a get_locale func """
    locale = request.args['locale']
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """ returns the index.html template """
    from flask_babel import gettext as _
    return render_template('5-index.html')


def get_user():
    """ returns a user dict or None if ID not found or login_as not passed """
    id = int(request.args['login_as'])
    if id is not None and id in users:
        return users[id]
    return None


@app.before_request
def before_request():
    """ gets user and sets it as a global(?) on flask.g.user """
    g.user = get_user()


if __name__ == '__main__':
    app.run()
