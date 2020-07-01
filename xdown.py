#!/usr/bin/env python3

import requests
import sys
import os
from lib import status
from lib import color
from src import mod_file
from src import mod_playlist
from src import quality

class settings:
    LINK = None
    PATH = None
    FILE = None
    PAGE = None

def launch(mod):
    settings.PATH = sys.argv[3]
    if settings.PATH[len(settings.PATH) - 1] == '/':
        settings.PATH[len(settings.PATH) - 1] = ''
    if os.path.isdir(settings.PATH) == False:
        os.mkdir(settings.PATH)
    if mod == "playlist":
        settings.LINK = sys.argv[1]
        settings.PAGE = sys.argv[4]
        return (mod_playlist.get(settings.LINK, settings.PATH, settings.PAGE))
    elif mod == "file":
        settings.FILE = sys.argv[1]
        return (mod_file.get(settings.FILE, settings.PATH))
    else:
        exit (84)

def __main__():
    if len(sys.argv) == 5:
        print("%s Playlist mod" % status.get("ok"))
        return (launch("playlist"))
    elif len(sys.argv) == 4:
        print("%s File mod" % status.get("ok"))
        return (launch("file"))
    else:
        print("%s  Usage:\n\
        File mod    : python3 xdown.py <File> -O <Output Folder>\n\
        Playlist mod: python3 xdown.py <Url>  -O <Output Folder> <Number of pages>\n\
        " % status.get("error"))
        return (-1)

__main__()
