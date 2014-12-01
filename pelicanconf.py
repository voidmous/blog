#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joshz'
SITENAME = u'JoshuaZhang'
SITEURL = ''
ARTICLE_URL = 'posts/{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}.html'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Python-Markdown extensions to be included
MD_EXTENSIONS = ['codehilite','extra','toc']

# Misc
GITHUB_URL= 'http://github.com/voidmous/'
PDF_GENERATOR = False

# Specify a customized theme, via relative path
THEME = "themes/tuxlite_tbs"

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/voidmous'),
          ('Douban', 'http://www.douban.com/people/45448149'),
          ('Weibo', 'http://weibo.com/u/1760438435'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# Must set to False in publishconf.py
RELATIVE_URLS = True

STATIC_PATHS = ['img', 'extra/robots.txt', 'extra/CNAME',]
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/robots.txt': {'path': 'robots.txt'},}
