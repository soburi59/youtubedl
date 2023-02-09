# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:30:30 2022

@author: 59195
"""

import re, sys, os, time, subprocess
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

main_links = [
"https://www.youtube.com/",
"https://soundcloud.com/",
"https://www.nicovideo.jp/"
]
url=input("url:")

# youtube soundcloud nicovideo
#main_linksのなかの一つでもurlに含まれていたらtrue
if any(s in url for s in (main_links)):
    #ans = input("type mp3 or mp4: ")
    if "https://www.youtube.com/" in url and "list=" in url:
        th_list = url.split("list=")[1]
    else:
        th_list = url
    num=input("何番目まで")
    cmd = f'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -i --playlist-end {num} --download-archive downloaded.txt --retries 3 --extract-audio --audio-format mp3 --add-metadata ' + th_list
    # if ans=="mp3":
    #     num=input("何番目まで")
    #     cmd = f'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -i --playlist-end {num} --download-archive downloaded.txt --extract-audio --audio-format mp3 --add-metadata ' + th_list
    # if ans=="mp4":
    #     cmd = 'youtube-dl -o ./%(playlist)s/%(title)s.%(ext)s -i -f mp4 --add-metadata ' + th_list
    subprocess.check_call(cmd.split())
    sys.exit()