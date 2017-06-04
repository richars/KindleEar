#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag
import datetime

def getBook():
    return Reuters
    

class Reuters(BaseFeedBook):
    title                 = 'Reuters North Korea'
    description           = 'Reuters North Korea'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_economist.gif" 
    coverfile             = "cv_economist.jpg"
    oldest_article        = 1
#    deliver_days          = ['Friday']
#    deliver_times         = [18]
    fulltext_by_readability = True
    keep_image            =  False
    
    def ParseFeedUrls(self):
        #return lists like [(section,title,url,desc),..]
        main = 'http://www.reuters.com/places/north-korea'
        urls = []
        isEST = False #判断是EST还是EDT
        opener = URLOpener(self.host, timeout=90)
        result = opener.open(main)
        if result.status_code != 200:
            self.log.warn('fetch webpage failed:%s'%main)
            return []
            
        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        
        #开始解析
        section=soup.find('div', attrs={'class':'topStory'})
        toparticle = section.find('a', href=True)
        if toparticle is None:
            self.log.warn('Top news not found')
        toptitle = string_of_tag(toparticle).strip()
        if not toptitle:
            self.log.warn('No top story title')
        url = toparticle['href']
        if url.startswith(r'/'):
            url = 'http://www.reuters.com' + url
        urls.append(('Reuters North Korea',toptitle,url,None))
            
        sect=soup.find('div', id='moreSectionNews')
        for feature in sect.find_all('div', attrs={'class':'feature'}):
            article = feature.find('a', href=True)
            title = string_of_tag(article).strip()
            url = article['href']
            timestamp = feature.find('span', attrs={'class':'timestamp'})
            if not timestamp:
                continue
            timestamp = string_of_tag(timestamp).strip()
            #今天的文章
            if 'EDT' in timestamp or 'EST' in timestamp:
                delta=0
                if 'EST' in timestamp:
                    isEST=True
            else:
                pubtime = datetime.datetime.strptime(timestamp, '%b %d %Y').date()
                #默认为EDT
                tnow = datetime.datetime.utcnow()-datetime.timedelta(hours=4)
                currentmonth= tnow.month
                if currentmonth in [1, 2, 12] or isEST:
                    tnow = datetime.datetime.utcnow()-datetime.timedelta(hours=5)
                tnow = tnow.date()
                delta=(tnow-pubtime).days
            if self.oldest_article > 0 and delta > self.oldest_article:
                continue
            if url.startswith(r'/'):
                url = 'http://www.reuters.com' + url
                #self.log.info('\tFound article:%s' % title)
            urls.append(('Reuters North Korea',title,url,None))
                                
        if len(urls) == 0:
            self.log.warn('len of urls is zero.')
        return urls
    
    extra_css= '''
    h1 {font-size: large; font-weight: bold}
    .article-subtitle { font-weight: bold }
    .module-caption {font-style: italic}
    '''
