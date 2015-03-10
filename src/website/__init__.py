#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Flask
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.config.from_pyfile('../config.py')

# Show debug information if app.debug = True
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

import website.views
