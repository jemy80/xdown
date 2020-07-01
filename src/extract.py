import requests
from src import video
from src import quality
from lib import status

def get(url, PATH):
    i = 0
    name = ""
    count = 0
    r = requests.get(url)

    if r.status_code != 200:
        print("%s Connection refused" % status.get("ko"))
        return (-1)
    tmp = quality.get(r.text)
    if tmp != 84:
        while i < len(tmp):
            if tmp[i] == "'":
                count += 1
            if count == 1 and tmp[i] != "'":
                name += tmp[i]
            if count == 2 and name != "":
                break
            i += 1
        video.download(name, url, PATH)