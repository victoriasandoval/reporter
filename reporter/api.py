#!/usr/bin/env python 
# coding=utf8

from flask import Flask
from reporter import header
app = Flask(__name__)

@app.route("/")
def hello():
    return header.create_header('data/authors.json', 'Paris XII')
