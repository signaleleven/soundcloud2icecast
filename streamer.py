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

api = SoundcloudAPI()

playlist = api.resolve('https://soundcloud.com/poolsidefm/sets/poolside-fm-official-playlist')
total=0
s = shout.Shout()
print("Using libshout version %s" % shout.version())
s.host = 'vpn.signal-eleven.com'
s.password = 'banana'
s.mount = "/stream"
s.format = 'mp3'
s.url = 'radio.signal-eleven.com'
s.genre = 'poolside music'
s.public = 0
s.name = 'Poolside PM'
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
def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


assert type(playlist) is Playlist                                                                                                                                         
while True:
    track=random.choice(playlist.tracks)
    if (datetime.datetime.fromtimestamp(time.time())-datetime.datetime.strptime(track.display_date[:10],"%Y-%m-%d")).days > 350:
        if random.random() > 0.5:
            print("Randomly skipping old track %s released %s" % (track.title, track.display_date))
            continue
    for transcode in track.media['transcodings']:
        if transcode['format']['protocol'] == "progressive":
            print(track.title)
            s.set_metadata({'song': track.title})
            url=get_obj_from(transcode['url'] + "?client_id=" + track.client.client_id)['url']
            filename = f'./{track.artist} - {track.title}'
            f=io.BytesIO(urlopen(url).read())
            nbuf = f.read(4096)
            while 1:
                buf = nbuf
                nbuf = f.read(4096)
                total = total + len(buf)
                #print(total)
                if len(buf) == 0:
                 print("end of song")
                 break
                s.send(buf)
                s.sync()
            f.close()
        else:
            print("skipping unplayable url")
