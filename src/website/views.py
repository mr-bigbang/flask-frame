#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import render_template

from website import app

@app.route('/')
def index():
    return render_template('index.html')
