#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import urllib2,urllib
web.config.debug = False
from post import postSite
from post import publish58
#from post import publishSoufang
#from post import publishAnjuke
#from fetch import threadControl
urls = (
        '/check_account', 'check_account',
        '/post_data', 'post_data',
        "/.*", "hello"
        )
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'good luck!'


def postDecode(post):
    result={}
    for i in post.split("&"):
        i=i.split("=",1)
        if len(i)==2:
            result[urllib.unquote(i[0])]=urllib.unquote(i[1])
    return result

class check_account:
    def POST(self):
        data = web.data()
        print data
        postData = postDecode(data)  
        try:            
            res = postSite.select(postData)            
        except:
            res = 'codeerror' 
            pass
        return res
    
class post_data:
    def POST(self):
        data = web.data()
        postData = postDecode(data)
        result=""
        try:
            if int(postData['webid'])==8:
                result = publish58.Publish(postData) 
            #elif int(postData['webid'])==3:
                #result = publishSoufang.Publish(postData)
            #elif int(postData['webid'])==4:
                #result = publishAnjuke.Publish(postData) 
            
        except Exception,e:
            return "1111%s"%e
        print result               
        return result

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()