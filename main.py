#!/usr/bin/env python
"""
main execute file
By Hito http://www.hitoy.org/
"""
def saveurl(urllist,urlfile):
    handle = open(urlfile,"a+")
    for url in urllist:
        print "http://%s"%url
        handle.write("http://%s\n"%url)
    handle.close()

def savekey(keylist):
    handel = open('alibabakey.txt',"a+")
    for i in keylist:
        handel.write("%s\n"%i)
    handel.close()


import get_url,getkey,sys,time
t = 20
count = 20000

if not sys.argv[1:]:
    keyword = raw_input("Must Input a keyword: ").strip()

if '-k' in sys.argv:
    k=sys.argv.index('-k')+1
    keyword = sys.argv[k]

if '-t' in sys.argv:
    t = sys.argv.index('-t')+1
    t = int(sys.argv[t])

while True:
    print "Get Alibaba Url......"
    if count < 0: break
    try:
        saveurl(get_url.List(keyword,count).listurl(),'urllist.txt')
    except:
        break
    time.sleep(t)
    count = count - 10


#open url list:
ul=open("urllist.txt","r")
print "Get Alibaba keyword....."
while True:
    url = ul.readline().strip()
    if not url: break
    keylist=getkey.getkey(url)
    if keylist:
        savekey(keylist)
        print 'Get %s success!'%url
    else:
        print 'Get %s Failed!'%url
    time.sleep(5)
ul.close()
        