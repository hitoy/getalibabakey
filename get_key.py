#!/usr/bin/env python
"""
Get alibaba key

By Hito Http://www.hitoy.org/
"""
import urllib2,re
def key(url,separator=", "):
    header={"Accept": "text/plain","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36","Referer":"https://www.google.com/"}
    if not url: return
    req = urllib2.Request(url,headers=header)
    try:
        page = urllib2.urlopen(req,timeout=10)
        content = page.read()
    except:
        content = ''

    if not content: return

    babare=re.compile(r'<title>(.*?)</title>',re.I|re.M)
    title = babare.findall(content)[0].rstrip(' at Alibaba.com')
    return title.split(separator)
