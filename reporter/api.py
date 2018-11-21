#!/usr/bin/env python
# coding=utf8

# imports
from flask import Flask
from reporter import header
from reporter.poem import Poem
import subprocess

# init Flask
app = Flask(__name__)
app.config.from_pyfile('../api.cfg')

# init Poem
poem = Poem(url=app.config['POEM_URL'], selector=app.config['POEM_SELECTOR'])
poem._fetch_poem()


# HTTP routing
@app.route("/")
def hello():
    markdown_file = header.create_header(app.config['AUTHOR_PATH'], 'Paris XII')
    subprocess.run()
    return header.create_header(app.config['AUTHOR_PATH'], 'Paris XII')

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
