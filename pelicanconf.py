#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Grupy-RP'
SITENAME = u'Grupy-RP'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

THEME = 'themes/malt'
SITE_LOGO = 'images/logo/logo.png'
SITE_BACKGROUND_IMAGE = 'images/banners/aerea.jpg'
STATIC_PATHS = ['images', ]

WELCOME_TITLE = 'Grupy-RP'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = "blog/index.html"

PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'members'
]


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

MALT_HOME = [
    {
        "color": "blue-grey lighten-5",
        "title": "O que Fazemos?",
        "items": [
            {
                "title": "Comunidade",
                "icon": "fa-comments",
                "text": "",
                "buttons": [
                    {
                        "text": "Saiba Mais",
                        "href": "comunidade",
                    },
                ],
            },
            {
                "title": "Membros",
                "icon": "fa-users",
                "text": "",
                "buttons": [
                    {
                        "text": "Conheça",
                        "href": "membros",
                    },
                ],
            },
            {
                "title": "Projetos",
                "icon": "fa-briefcase",
                "text": "",
                "buttons": [
                    {
                        "text": "Mais detalhes",
                        "href": "http://github.com/grupyrp/",
                    },
                ],
            },
        ]
    },
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
