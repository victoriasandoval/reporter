#!/usr/bin/env/python
# coding=utf8

import pytest
import requests
import os
import tempfile
from pathlib import Path
from reporter.reportergenartor import ReporterGenerator
import matplotlib

matplotlib.use('Agg')

def test_reporter():

    module_dir = os.path.abspath(os.path.dirname(__file__))
    module_dir = Path(module_dir)/'../data'
    gene = ReporterGenerator(module_dir)
    gene.addheader()
    gene.addplot()
    gene.build_result()
    #assert (module_dir/'../data/markdown.md').is_file
