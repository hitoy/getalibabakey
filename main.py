#!/usr/bin/env python
"""
main execute file
By Hito http://www.hitoy.org/
"""
import  get_url,get_key,sys,time,fcntl

def saveurl(urllist,urlfile):
    handle = open(urlfile,"a+")
    fcntl.flock(handle,fcntl.LOCK_EX)
    for url in urllist:
        print "http://%s"%url
        handle.write("http://%s\n"%url)
    fcntl.flock(handle,fcntl.LOCK_UN)
    handle.close()


def savekey(keylist):
    handle = open('alibabakey.txt',"a+")
    fcntl.flock(handle,fcntl.LOCK_EX)
    for i in keylist:
        handle.write("%s\n"%i)
    fcntl.flock(handle,fcntl.LOCK_UN)
    handle.close()

def geturl(page):
    try:
        if page > 500: return
        urllist=get_url.List(keyword,page).listurl()
        if urllist:
            saveurl(urllist,'urllist.txt')
        time.sleep(t)
        page = page + 1
        return geturl(page)
    except KeyboardInterrupt,e:
        return

def getkey():
    ul=open("urllist.txt","r")
    while True:
        try:
            url = ul.readline().strip()
            if not url: break
            keylist=get_key.key(url)
            if keylist:
                savekey(keylist)
                print 'Get %s success!'%url
            else:
                print 'Get %s Failed!'%url
            time.sleep(5)
        except KeyboardInterrupt,e:
            break
    ul.close()

t = 10
page = 1
        
if not sys.argv[1:]:
    keyword = raw_input("Must Input a keyword: ").strip()

if '-k' in sys.argv:
    k=sys.argv.index('-k')+1
    keyword = sys.argv[k]

if '-t' in sys.argv:
    t = sys.argv.index('-t')+1
    t = int(sys.argv[t])
if not 'getkey' in sys.argv:
    geturl(page)
else:
    print "Get Alibaba keyword....."
    getkey()
