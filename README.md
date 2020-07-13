Simple python script to stream to an icecast/shoutcast server songs from a SoundCloud playlist.
It's biased towards new tracks. When a track is older than 350 days, it has a 50% chance of being skipped.
This behavior will be configurable in the future.

The code is very bad, it started as an experiment and PRs are welcome to straighten it up.

Based on: 
 - https://github.com/3jackdaws/soundcloud-lib
 - https://github.com/yomguy/python-shout

Optional Icecast server (for testing or self hosting - seems abandoned)
 - https://github.com/infiniteproject/icecast


Usage
-----

- edit `docker-compose.yaml` to select the playlist(s) to stream
- `docker-compose up`
