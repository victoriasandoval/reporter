#!/usr/bin/env/python
# coding=utf8

import pytest
import requests
from reporter.poem import Poem


def test_fetch_poem():

    # ko, wrong url
    bad_poem = Poem(url="http://fake.tld")
    with pytest.raises(requests.exceptions.ConnectionError):
        bad_poem._fetch_poem()

    # ok, good url (use the default, :blink:)
    good_poem = Poem()
    good_poem._fetch_poem()
    assert good_poem.elements is not None
    assert 0 < len(good_poem.elements)
