#!/usr/bin/env python

# imports
from requests_html import HTMLSession


class Poem():

    def __init__(self,
            url="https://fr.wikisource.org/wiki/Po%C3%A9sies_(Rimbaud)/%C3%A9d._Vanier,_1895/Le_Bateau_ivre",
            proxies={'http': None, 'https': None}):
        self.proxy = proxies
        self.url = url
        self.session = HTMLSession()
        self.poem = []

    def _fetch_poem(self):
        r = self.session.get(self.url, proxies=self.proxy)
        self.poem = [poem.text for poem in r.html.find("div.poem")]
