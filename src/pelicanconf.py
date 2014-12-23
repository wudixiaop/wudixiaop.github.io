#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rocky Lai'
SITENAME = u"Rocky Lai @ Github"
SITEURL = '.'
THEME = "Theme/CleanBlog"

PATH = 'content'

TIMEZONE = 'Asia/Chongqing'

DEFAULT_LANG = u'en-us'
# 根据上面的DEFALUT_LANG来匹配日期格式
DATE_FORMATS = {
    'en-us': '%Y-%m-%d %H:%M',
}    

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ("Rocky's Github", "https://github.com/wudixiaop"),
    ("ShaderlabVS Downloads", "http://wudixiaop.github.io/shaderlabvs-release-page.html"),
    )

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
DISQUS_SITENAME = "wudixiaopgithubio"

#CLEAN-BLOG THEME
COLOR_SCHEME_CSS = "github.css"
#HEADER_COVER = 'static/my_image.png'
SITESUBTITLE = "心亡则忙，亡心则忘"
