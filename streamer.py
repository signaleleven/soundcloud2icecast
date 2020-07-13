from sclib import SoundcloudAPI, Track, Playlist
from urllib.request import urlopen
import json
import unicodedata
import re
import shout
import io
import time
import random
import datetime
import os 

api = SoundcloudAPI()

playlist = api.resolve(os.environ.get('SOUNDCLOUD_PLAYLIST'))
s = shout.Shout()
print("Using libshout version %s" % shout.version())
s.host = os.environ.get('ICECAST_HOST')
s.password = os.environ.get('ICECAST_PASSWORD')
s.mount = os.environ.get('ICECAST_MOUNTPOINT','/stream')
s.format = 'mp3'
s.url = os.environ.get('ICECAST_URL', "unknown")
s.genre = os.environ.get('ICECAST_GENRE', "unknown")
s.public = os.environ.get('ICECAST_PUBLIC', 0) 
s.name = os.environ.get('ICECAST_STREAM_NAME', "unknown")
s.description = os.environ.get('ICECAST_STREAM_DESCRIPTION', "No Description")
s.open()

def get_url(url):
    return urlopen(url).read()

def get_page(url):
    return get_url(url).decode('utf-8')

def get_obj_from(url):
  try:
      return json.loads(get_page(url))
  except Exception as e:
      return False                                                                                                                                                      
assert type(playlist) is Playlist                                                                                                                                         
while True:
    track=random.choice(playlist.tracks)
    if (datetime.datetime.fromtimestamp(time.time())-datetime.datetime.strptime(track.display_date[:10],"%Y-%m-%d")).days > 350:
        if random.random() > 0.5:
            print("Randomly skipping old track %s released %s" % (track.title, track.display_date))
            continue
        else:
            print("Randomly allowing old track %s released %s" % (track.title, track.display_date))
    for transcode in track.media['transcodings']:
        if transcode['format']['protocol'] == "progressive":
            print(track.title)
            s.set_metadata({'song': track.artist + " - " + track.title + ' / ' + track.uri})
            url=get_obj_from(transcode['url'] + "?client_id=" + track.client.client_id)['url']
            f=io.BytesIO(urlopen(url).read())
            nbuf = f.read(4096)
            while 1:
                buf = nbuf
                nbuf = f.read(4096)
                if len(buf) == 0:
                 print("end of song")
                 break
                s.send(buf)
                s.sync()
            f.close()
        else:
            print("skipping unplayable url for " + track.title)
