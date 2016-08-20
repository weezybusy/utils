#!/usr/bin/env python3
# encoding: utf-8

import urllib.request
import sys

def translate(string, to_lang="auto", from_lang="auto"):
    before_trans = 'class="t0">'
    url = "http://translate.google.com/m?hl={}&sl={}&q={}".format(to_lang, from_lang, string)
    agent = { 'User-Agent': 'Mozilla/5.0', 'Accept-Charset': 'utf-8' }
    request = urllib.request.Request(url, headers=agent)
    page = urllib.request.urlopen(request).read().decode("utf-8")
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return result

def main():
    if len(sys.argv) < 2:
        print('Nothing to translate.')
        sys.exit(0)
    string = '+'.join(sys.argv[1:])
    result = translate(string, "ru")
    print('> ' + result)

if __name__ == '__main__':
    main()
