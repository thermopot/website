#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Potentials'
SITENAME = 'ThermoPot - interatomic potential database'
SITEURL = 'http://thermopot.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Modifications 
IGNORE_FILES = [".ipynb_checkpoints"]
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{category}/{slug}/"
PAGE_SAVE_AS = "{category}/{slug}/index.html"
OUTPUT_PATH = "../public/"

# Plugins and extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.toc': {
            'permalink': 'true'
        },
        'markdown.extensions.meta': {},
        'markdown.extensions.admonition': {},
    }
}

# Theme modifications
THEME = "themes/elegant"
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Home page 
DISPLAY_PAGES_ON_MENU = False

# Theme fixes
TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
ARCHIVES_URL = "archives.html"

# Add sitemap to support search
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins 
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'liquid_tags', 'pelican-ipynb.liquid', 'tipue_search']
