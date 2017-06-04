#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Solidot

class Solidot(BaseFeedBook):
    title                 = u'Solidot'
    description           = u'Solidot'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ftchinese.gif"
    coverfile             = "cv_ftchinese.jpg"
    oldest_article        = 1
    keep_image            = False
    extra_css      = '''
        body { font-size: 1em;  text-align: justify;  line-height: 1.718em}
        p { font-size: 1em;  text-align: justify;  line-height: 1.718em }
        div { font-size: 1em;  text-align: justify;  line-height: 1.718em }
        h1 { font-size: large  }
        '''
    
    feeds = [
            (u'Solidot', 'http://feeds.feedburner.com/solidot'),
            ]
    
        