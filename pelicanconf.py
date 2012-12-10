#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"voidmous"
SITENAME = u"幻空轩"
SITEURL = 'http://voidmous.github.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'cn'

# Misc
GITHUB_URL= 'http://github.com/voidmous/'
PDF_GENERATOR = False

# Specify a customized theme, via relative path
THEME = "./themes/tuxlite_tbs"

# RSS and ATOM
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/voidmous'),
          ('Twitter', 'https://twitter.com/voidmous'),
          ('Douban', 'http://www.douban.com/people/45448149'),
          ('Weibo', 'http://weibo.com/u/1760438435'),
          ('Renren', 'http://www.renren.com/221168912'),)

DEFAULT_PAGINATION = 10

# https://github.com/getpelican/pelican/wiki/Tips-n-Tricks
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
                 ('extra/favicon.ico', 'favicon.ico'),)
