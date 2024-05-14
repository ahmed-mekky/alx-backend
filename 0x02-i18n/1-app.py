#!/usr/bin/env python3
"""Python Script"""
from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
