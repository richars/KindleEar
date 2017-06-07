#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return NYTChinese

class NYTChinese(BaseFeedBook):
    title                 = u'纽约时报中文网'
    description           = u'纽约时报中文网'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_ftchinese.gif"
    coverfile             = "cv_ftchinese.jpg"
    oldest_article        = 1
    keep_image            = True
    extra_css      = '''
        body { font-size: 1em; text-align: justify;  line-height: 1.618em; margin: 0; }
        p { font-size: 1em; text-align: justify;  line-height: 1.618em; }
        h1 { font-size: large; }
        '''
    
    feeds = [
            (u'纽约时报中文网', 'https://cn.nytimes.com/rss.html'),
            ]
    
        
