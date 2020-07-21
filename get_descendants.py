#!/usr/bin/python3
from bs4 import BeautifulSoup
with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    root = soup.body
    root_childs = [e.name for e in root.descendants if e.name is not None]
    print(root_childs)