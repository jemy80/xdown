import requests
import os
from lib import status
from lib import color
from src import quality
from src import extract

class content:
    LINKS = []

def proof(DATA):
    url = ""
    base = "https://www.xvideos.com"
    click = "prof-video-click"

    DATA.split(click)
    print(DATA)
    exit(0)
    for i in range(0, len(DATA)):
        for j in range(0, len(DATA[i])):
            if DATA[i][j] != '"' or DATA[i][j] != '\'':
                print(url)
                url += DATA[i][j]
            else:
                print("%s/%s%s" % (base, click, url))
                content.LINKS.append("%s/%s%s" % (base, click, url))
                url = ""
                break

def get(FILE, PATH, PAGE):
    for i in range(1, int(PAGE)):
        print("Page: %s" % i)
        r = requests.get("%s#%d" % (FILE, i))
        print("%s#%d" % (FILE, i))
        if r.status_code == 200:
            proof(r.text)
        else:
            print("%s Connection refused" % status.get("ko"))
    for i in range(0, len(content.LINKS)):
        extract(content.LINKS[i], PATH)