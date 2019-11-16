# ydl1.py
from __future__ import unicode_literals
import youtube_dl
import sys
from sys import *

def main() :
	p = stdin.readline()
	p = p.strip('\n')
	p='https://www.youtube.com/watch?v=aJOTlE1K90k'
	ydl_opts = {
            'format': 'bestaudio/best', 
                   'format': 'bestaudio/best',
               'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '320',
             }],
                }
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(p)])
	#ydl.download([p])
if __name__=='__main__' :
	main()
