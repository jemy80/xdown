#!/usr/bin/env python3

import requests
import sys
import os
from src import video
from src import extract

class settings:
    URL  = None
    HREF = None

def __count__(DATA, c):
    count = 0

    for i in range(0, len(DATA)):
        if DATA[i] == c:
            count += 1
    return (count)

def clean(line):
    ref = ""
    count = 0
    i = 0

    while i < len(line) and count != 1:
        if line[i] == '"' or line[i] == '\n':
            count += 1
        if count == 0 and line[i] != '"':
            ref += line[i]
        i += 1
    return (ref)

def resume_href(array):
    i = 0

    while i < len(array):
        if array[i].startswith("/video") and __count__(array[i], '/') > 1:
            extract.get("%s%s" % (settings.HOST, array[i]), settings.HREF)
        i += 1

def parse_href(r):
    current = None
    count = 0
    i = 1
    data = r.text.split('href="')
    href = []

    while i < len(data):
        if len(data[i]) >= 1:
            href.append(clean(data[i]))
            count += 1
        i += 1
    resume_href(href)

def connect():
    try:
        r = requests.get(settings.URL)
        if r.status_code == 200:
            parse_href(r)
    except:
        exit(-1)

def get(url, PATH):
    settings.HREF = PATH
    settings.URL = url
    if url.startswith("https://www.xvideos.com"):
        settings.HOST = "https://www.xvideos.com"
    elif url.startswith("https://www.xnxx.com"):
        settings.HOST = "https://www.xnxx.com"
    else:
        print("Can't do that with this website")
        exit(-1)
    connect()
    return (0)