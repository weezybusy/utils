import sys
import webbrowser

if len(sys.argv) < 2:
    sys.exit(0)

youtube = 'https://www.youtube.com/results?search_query='
it = '+'.join(sys.argv[1:])

webbrowser.open(youtube + it)
