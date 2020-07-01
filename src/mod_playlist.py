import requests
import os
from lib import status
from lib import color
from src import quality
from src import extract
from src import referencer

def get(LINK, PATH, PAGE):
    PAGE = int(PAGE)

    if PAGE < 1:
        print("I can't do less than 1 page")
        return (-1)
    else:
        for i in range(1, PAGE):
            referencer.get("%s/%s" % (LINK, i), PATH)
        return (0)