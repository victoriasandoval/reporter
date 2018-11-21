#!/usr/bin/env python
# coding=utf8

# imports
from flask import Flask, render_template
from reporter import header
from reporter.reportergenartor import ReporterGenerator
from reporter.poem import Poem
from pathlib import Path
import subprocess
import json

# init Flask
app = Flask(__name__)
app.config.from_pyfile('../api.cfg')

# init Poem
poem = Poem(
    url=app.config['POEM_URL'],
    selector=app.config['POEM_SELECTOR'],
    proxies={
        'http': app.config['HTTP_PROXY'],
        'https': app.config['HTTPS_PROXY']
    }
)
poem._fetch_poem()

# file path
data_path = Path(app.config['DATA_PATH'])
json_file = data_path/app.config['INPUT_FILE']
markdown_file = data_path/app.config['MD_FILE']
html_file = data_path/app.config['OUTPUT_FILE']

# HTTP routing
@app.route("/")
def hello():
    # Generate markdown file in data/
    gen = ReporterGenerator(app.config['DATA_PATH'])
    gen.addheader()
    gen.addplot()
    gen.build_result()

    # strophe

    strophe = poem.rand_strophe()
    with open(markdown_file, 'a') as file:
        file.write('\n\n' + strophe)

    # Generate HTML File
    html_cmd = f"""pandoc {markdown_file} -o {html_file}"""
    subprocess.run(html_cmd.split(' '))

    # ouin
    with open(html_file, 'r') as file:
        return(file.read())

    # this should work but "template not found error"
    #return(render_template(str("index.html")))


if __name__ == "__main__":
    app.run(
        ssl_context='adhoc',
        #static_folder=data_path,
        #template_folder=data_path
    )
