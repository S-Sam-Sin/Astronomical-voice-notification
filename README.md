# Astronomical Voice Notification
(full description coming soon)
## Requirements
`sudo apt-get install -y python3-dev libasound2-dev`<br>
`sudo apt install mplayer`<br>
`sudo pip3 install simpleaudio`<br>
`sudo pip3 install pyephem`<br><br>
## Getting Started
Go to your home directory<br>
`cd ~/`<br>
Turn LIRC support for Mplayer off<br>
`echo "nolirc=yes" >> .mplayer/config`<br>
(This section is NOT finished)
## Special Thanks and Credits
- Astronomical computations : [PyEphem](http://rhodesmill.org/pyephem/)
- Voice : [Mary Web Client](http://mary.dfki.de:59125)<br>
Voice used : `dfki-spike-hsmm en_GB male hmm`