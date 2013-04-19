#!/usr/bin/env python
# -*- coding: utf8 -*-

from spoddit import SpodditSessionManager 

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
    session_m.connect()
    session_m.disconnect()
