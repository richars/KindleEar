#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag
import urllib

def getBook():
    return TheEconomist
    

def fetch_cover(self):
    mainurl = 'http://www.economist.com/printedition'
    opener = URLOpener(None, timeout=90)
#    opener = URLOpener(self.host, timeout=90)
    result = opener.open(mainurl)
    content = result.content.decode('utf-8')
#    content = result.content.decode(self.feed_encoding)
    soup = BeautifulSoup(content, "lxml")
    div=soup.find('div', attrs={'class':'print-edition__cover-widget'})
    img = div.find('img', src=True)
    cover = img.get('src')
    if cover.startswith('/'):
        cover = 'http://www.economist.com' + cover
    data = urllib.urlopen(cover).read()
    return data

class TheEconomist(BaseFeedBook):
    title                 = 'The Economist Web'
    description           = 'Global news and current affairs from a European perspective, delivered on Friday.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_economist.gif" 
#    coverfile             = "cv_economist.jpg"
    coverfile             =  fetch_cover
    deliver_days          = ['Friday']
    deliver_times         = [18]
    fulltext_by_readability = False
    keep_image            = True
    
    remove_classes = ['ec-messages', 'dblClkTrk', 'ec-article-info',
                      'share_inline_header', 'related-items','pullquote','ad-panel__googlead'
                      'ec-gallery-carosel','footnotes','yj6qo ajU','esi-generated pullquote',
                      'ec-topic-widget fullwidth medium','ec-article-info source','blog-post__comments-label',
                      'blog-post__section-date-author','blog-post__foot-note','link-button sections-card__link',
                      'sections-card__list-item','latest-updates-panel__footer latest-updates-panel__footer--blog-post',
                      'latest-updates-panel__label latest-updates-panel__label--blog-post','latest-updates-panel__body',
                      'latest-updates-panel-card__wrapper','latest-updates-panel__article-link','latest-updates-panel-card',
                      'atest-updates-panel-card__body','latest-updates-panel-card__title','latest-updates-panel-card__subtitle',
                      'latest-updates-panel-card__time','blog-post__siblings-list-aside ','blog-post__siblings-list-aside',
                      'blog-post__siblings-list-header ','blog-post__siblings-list-header','special-report-header',
                      'special-report-header-sponser','content_clearfix','column-right','blog-post__asideable-wrapper'
                      ]
#    remove_ids = ['more-kallery']
    remove_tags = [
            {'name':'script'},{'name':'noscript'},{'name':'aside'}
    ]
    keep_only_tags = [{'name':'article'}
                     ]
    remove_tags_after = [ dict(attrs={'class':['blog-post__foot-note','blog-post__comments-label']})
    ]
    remove_attributes = ['data-reactid']
    feeds = [
            ('Index', 'http://www.economist.com/printedition'),
           ]
    
    def ParseFeedUrls(self):
        #return list like [(section,title,url,desc),..]
        main = 'http://www.economist.com/printedition'
        urls = []
        urladded = set()
        opener = URLOpener(self.host, timeout=90)
        result = opener.open(main)
        if result.status_code != 200:
            self.log.warn('fetch webpage failed:%s'%main)
            return []
            
        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        
        #开始解析
        for section in soup.find_all('li', attrs={'class':'list__item'}):
            div = section.find('div')
            if div is None:
                self.log.warn('This part skipped.')
                continue
            sectitle = string_of_tag(div).strip()
            if not sectitle:
                self.log.warn('No section title')
                continue
            if sectitle == 'Economic and financial indicators':
                continue
            #self.log.info('Found section: %s' % section_title)
            articles = []
            for node in section.find_all('a', href=True):
                spans = node.findAll('span')
                if len(spans) == 2:
                    fly= node.find('span', attrs={'class':'print-edition__link-flytitle'})
                    pre= string_of_tag(fly).strip()
                    ti= node.find('span', attrs={'class':'print-edition__link-title'})
                    post= string_of_tag(ti).strip()
                    title = pre +': '+ post
                else:
                    title = string_of_tag(node).strip()
                url = node['href']
                if url.startswith(r'/'):
                    url = 'http://www.economist.com' + url
                    #self.log.info('\tFound article:%s' % title)
                    if url not in urladded:
                        urls.append((sectitle,title,url,None))
                        urladded.add(url)
                                
        if len(urls) == 0:
            self.log.warn('len of urls is zero.')
        return urls
    
    extra_css= '''
    .flytitle-and-title__flytitle {font-size: large; font-weight: bold}
    .flytitle-and-title__title {font-size: large; font-weight: bold}
    .blog-post__rubric { font-weight: bold;  }
    figcaption {font-style: italic}
    .caption {font-style: italic}
    .location { font-size: small;  }
    .xhead { font-weight: bold;  }
    .Bold { font-weight: bold; font-style: normal }
        '''
