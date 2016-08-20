#!/usr/bin/env python3
# encoding: utf-8

import urllib.request
import sys

agent = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_langage="auto", langage="auto"):
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
    request = urllib.request.Request(link, headers=agent)
    page = urllib.request.urlopen(request).read().decode("utf-8")
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return(result)

def main():
    if len(sys.argv) < 2:
        print('Nothing to translate.')
        sys.exit(0)
    string = ' '.join(sys.argv[1:])
    result = translate(string, "ru")
    print('> ' + result)

if __name__ == '__main__':
    main()
