from typing import List

import requests
from Component.MySoup import BeautifulSoup
from Component import Element


class Website:
    content: List[Element.Element]
    oBody: BeautifulSoup or None
    title: str
    url: str

    def __init__(self, url):
        self.url = url
        self.bs = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        self.title = ''
        self.oBody = None
        self.content = []
