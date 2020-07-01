import os
from lib import status
from src import video
from src import extract

def get(FILE, PATH):
    if os.path.exists(FILE):
        f = open(FILE, 'r')
        line = f.readline()
        while line:
            if len(line) > 1:
                extract.get(line, PATH)
                line = f.readline()
        f.close()
    else:
        print("%s File not found" % status.get("error"))
        return (-1)