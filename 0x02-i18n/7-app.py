#!/usr/bin/env python3
"""Python Script"""
from flask import Flask, render_template, g
from flask_babel import Babel
from flask import request
import pytz


class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """get user"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@app.before_request
def before_request():
    """before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """get timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        return g.user.get('timezone')
    return app.config['BABEL_DEFAULT_TIMEZONE']
@app.route('/')
def index():
    """index func"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
