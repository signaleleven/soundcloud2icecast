Simple python script to stream tracks from a Soundcloud playlist to an icecast/shoutcast server.
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
- edit `docker-compose.yaml` to select the playlist(s) to stream and configure the passwords and hostname for the icecast server
- `docker-compose up`
- connect any suitable player to the exposed port of the icecast server (whether started as part of this project, or remote)

License
-------
See `LICENSE.txt`

Todo
----
- Add ssl frontend (traefik?)
- Disable admin path (does icecast support it or traefik?)


Disclaimer
----------
I started this project to scratch my own itch of having the tracks from [the awesome poolside.fm](https://poolside.fm) streamed to my kitchen, where I could only reliably stream shoutcast/icecast sources. 
