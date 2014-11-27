An interface to Winamp using python 3.

This is a fork of https://code.google.com/p/pywinamp/ which seems to be abondened. Original author release note:
http://ingeration.blogspot.de/2008/05/python-winamp-control-module.html

###New Functions & Fixes:
`getListPosition()` - Returns the current position in the active playlist.

`getPlayingFilename()` - Gets the filename of the currently playing track.

Better handling of the *Playlist Window* - The previous implementation didn't handle the newly added functions correctly, because it differed from the way the Winamp API is intended to be used.

###Installation & Usage

    cd /home/you/pywinamp
    git clone https://bitbucket.org/freeo/pywinamp 
    py setup.py install

#####Example

    import pywinamp.winamp as pyamp
    w = pyamp.Winamp()

    title = w.getCurrentPlayingTitle()
    filename = w.getPlayingFilename()
    currentpos = w.getListPosition()

    print(title, filename, currentpos)

Requirements: ctypes, pywin32, Winamp 5+
