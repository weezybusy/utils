import sys
import webbrowser

if len(sys.argv) < 2:
    sys.exit(0)

google = 'https://www.google.com.ua/search?q='
it = '+'.join(sys.argv[1:])

webbrowser.open(google + it)
