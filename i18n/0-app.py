#!/usr/bin/env python3
""" setup a basic Flask app """
from flask import Flask

app = Flask(__name__)

@app.route('/')
