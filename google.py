#!/usr/bin/python3
# google.py -- Opens google page with search results for provided keywords.

import sys
import webbrowser

if len(sys.argv) < 2:
    print('Next time add some keyword, stupid.')
    sys.exit(0)

google = 'https://www.google.com.ua/search?q='
it = '+'.join(sys.argv[1:])
webbrowser.open(google + it)
