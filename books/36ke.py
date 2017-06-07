#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return Ke36

class Ke36(BaseFeedBook):
    title                 = u'36氪'
    description           = u'36氪'
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
            (u'36氪', 'http://www.36kr.com/feed?1.0',True),
            ]
    
#全文内容
        
