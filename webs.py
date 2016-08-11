#!/usr/bin/python3
# webs.py - Opens tabs with web pages I use constantly.

import webbrowser

pages = [ 'https://github.com/weezybusy',
          'https://keep.google.com',
          'https://translate.google.com.ua',
          'https://mail.google.com/mail/u/0/#inbox',
          'https://www.youtube.com',
          'https://www.khanacademy.org',
          'https://www.reddit.com',
          'http://clc-wiki.net/wiki/K%26R2_solutions' ]

for page in pages:
    webbrowser.open_new_tab(page)
