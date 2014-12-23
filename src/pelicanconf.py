#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rocky Lai'
SITENAME = u"Rocky Lai @ Github"
SITEURL = 'http://wudixiaop.github.io'
THEME = "Theme/CleanBlog"

WEB_SITE_DOMAIN = "http://wudixiaop.github.io" 

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'en-us'
# 根据上面的DEFALUT_LANG来匹配日期格式
DATE_FORMATS = {
    'en-us': '%Y-%m-%d %H:%M',
}

#通用    
DISQUS_SITENAME = "wudixiaopgithubio"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Bootstrap3
# Blogroll
#LINKS = (
#    ("Rocky's Github", "https://github.com/wudixiaop"),
#    ("ShaderlabVS Downloads", "http://wudixiaop.github.io/shaderlabvs-release-page.html"),
#    )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# 自我介绍
ABOUT_ME = """
I'm a coder in China.<br/>
"""

#SHOW_ARTICLE_AUTHOR = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True


#CLEAN-BLOG THEME
COLOR_SCHEME_CSS = "github.css"
SITESUBTITLE = "心亡则忙，亡心则忘"
GITHUB_URL = 'https://github.com/wudixiaop'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
