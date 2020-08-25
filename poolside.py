from sclib import SoundcloudAPI, Track, Playlist
from urllib.request import urlopen
import urllib
import json
import unicodedata
import jq

def get_url(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    return con.read()


def get_page(url):
    return get_url(url).decode('utf-8')

def get_obj_from(url):
  try:
      return json.loads(get_page(url))
  except Exception as e:
      return False              



def get_tracks(playlist_slug):
  api=get_obj_from("https://api.poolsidefm.workers.dev/v1/get_tracks_by_playlist")
  return jq.compile('.["payload"][]|select(.slug=="'+playlist_slug+'")["tracks_in_order"][]|.permalink_url').input(api).all()

