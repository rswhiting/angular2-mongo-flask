# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for module."""


import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_security import Security, utils

from .app_utils import utilities
from .config import CONFIG
from .models import User, db, user_datastore


def create_app():
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])
    utilities.setup_logger()
    db.init_app(app)
    Security(app, user_datastore)
    CORS(app, headers=['Content-Type'])

    return app


def create_user(app):
    user_datastore.create_user(
        email=app.config['ADMIN_USER'],
        password=utils.encrypt_password(app.config['ADMIN_PASSWORD']))
