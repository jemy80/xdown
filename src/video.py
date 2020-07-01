import os
from lib import status
from lib import color

def __slashes__(url):
    i = 0
    slash = 0

    if url[len(url) - 1] == '/':
        url[len(url) - 1] = ''
    while i < len(url):
        if url[i] == '/':
            slash += 1
        i += 1
    return (slash)

def download(video, url, PATH):
    crop = url.split('\n')[0]
    out = "%s.mp4" % crop.split('/')[__slashes__(crop)]
    
    if url.startswith("https://www.xnxx.com/"):
        print("%s Domain:%s  XNXX%s" % (status.get("info"), color.get("blue", 1), color.get("reset")))
    elif url.startswith("https://www.xvideos.com/"):
        print("%s Domain:%s  XVIDEOS%s" % (status.get("info"), color.get("red", 1), color.get("reset")))
    try:
        print("%s Output directory: '%s%s%s'" % (status.get("info"), color.get("purple", 1), PATH, color.get("reset")))
        print("%s Downloading '%s%s%s'" % (status.get("working"), color.get("purple", 1), out, color.get("reset")))
        os.system("wget -O %s/%s '%s' -q" % (PATH, out, video))
        print("%s Downloaded '%s%s%s'" % (status.get("ok"), color.get("purple", 1), out, color.get("reset")))
        return (0)
    except:
        print("%s Download failed" % status.get("error"))
        return (-1)