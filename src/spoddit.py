#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import thread

from spotify.manager import SpotifySessionManager
from spotify import Session, Link
from spotify import Playlist

f = open('htmlfiles/triphop','w')

trackList = [ ]
Playlist = None
song_listd = ['you dont + sil vous play', 'hairy trees + goldfrapp', 'hop track i made. distant echo + a trip', 'queen + magnolia', 'clouds + one of my latest tracks, i hope you all like it: uvb76', 'tapedeck sound + hermitude', 'fi sci + tom farrango', 'anita berber + death in vegas', 'static society + king kooba', 'near light + \xc3\x93lafur arnalds', 'glittered ripples from the depths + the synthetic dream foundation', 'esta + natural mystic', 'the last leaving man + tassel &amp; naturel', 'tattered and torn + egadz', 'killer bee + dj yas', 'slowly + tricky', 'afterglow + emancipator', 'attack the doctor + blockhead', 'claire + io', 'smile + eyedea &amp; abilities', 'man fat + bows', 'ten tigers + bonobo', 'between the bars + elliott smith', 'ki + dj krush &amp; toshinori kondo', 'leafroad + blacknight', 'unexpected consequence + 7thgalaxy', 'tell me how you feel + bonobo', 'hospihaze + blacknight', 'go outside + cults', 'xanxabar + blacknight', 'stream before album release...... + tokimonstas new album half shadows pre', 'lights + archive', 'black lake + emancipator', 'time to go + wax tailor', 'dreamsters + blacknight', 'lotus eaters + moloko', 'coffee &amp; sushi: 4/6/2013 + dj rbitrate', 'down + chinese man', 'science is my girlfriend + neat beats', 'sleeple... + found this today its got a touch of the future to it ~~~flume', 'most wanted man + dj krush', 'put it on tape + the herbaliser', 'buried mix 2 + flying lotus', 'moments ep + aleos', 'eastwood ft. gorillaz + moai', 'towers + bonobo', 'mr chimp on soundcloud + bank holiday breakbeat', 'call out my name + freddie joachim', 'soul city + bowery electric', 'as i moved on + blue foundation', 'hop radio show on wvkr when this pos... + tune in to downtime, my weekly trip', '6 underground + sneaker pimps', 'the ark + balus', 'on the dub + dj krush', 'rattlesnakes + emancipator', 'at the river + groove armada', 'borneo function + aydio', 'slip into something + kinobe', 'animal magic + bonobo', 'recurring + bonobo']




class SpodditSessionManager(SpotifySessionManager):
    queued = False
    playlist = 2
    track = 0
    appkey_file = os.path.join(os.path.dirname(__file__), 'spotify_appkey.key')
    

    def __init__(self, *a, **kw):
        SpotifySessionManager.__init__(self, *a, **kw)
        self.playlist = None
        self.track = None
        self.results = False


    def logged_in(self, session, error):
	if error:
	    print error
	    return
	print "Logged in!"
	S1=Search()
	for item in song_listd: 
	    S1.do_search(session,item)
	
	
	

    def logged_out(self, session):
	print "Logged out!"
	

class Search(SpotifySessionManager):

    def __init__(self):
	pass

	
    def add_track_results(self):
        print "Tracks:"
        tracklist=self.results.tracks()
        print "    ", str(Link.from_track(tracklist[0], 0))[14:], tracklist[0].name()	
	f.write(str(Link.from_track(tracklist[0], 0))[14:]+',')	
	trackList.append(tracklist[0])
	print len(trackList)


	
    def do_search(self,session, line):
        if not line:
            if self.results is False:
                print "No search is in progress"
            elif self.results is None:
                print "Searching is in progress"
            else:
                for a in self.results.tracks():
                    print "    ", Link.from_track(a, 0), a.name()
                print "%d tracks not shown" % (
                    self.results.total_tracks() - len(self.results.tracks()))
        else:
            line = line.decode('utf-8')
            self.results = None

            def search_finished(results, userdata):
                print "\nSearch results received"
                self.results = results
                self.add_track_results()
                

            session.search(line, search_finished)


if __name__ == '__main__':
    import optparse
    op = optparse.OptionParser(version="%prog 0.1")
    op.add_option("-u", "--username", help="Spotify username")
    op.add_option("-p", "--password", help="Spotify password")
    op.add_option(
        "-v", "--verbose", help="Show debug information",
        dest="verbose", action="store_true")
    (options, args) = op.parse_args()
    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    session_m = SpodditSessionManager(options.username, options.password, True)
    thread.start_new_thread(session_m.connect())
    session_m.disconnect()
	
