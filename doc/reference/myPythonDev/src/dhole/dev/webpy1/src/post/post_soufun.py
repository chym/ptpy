#!/usr/bin/env python
#-*- coding:utf-8 -*-

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2,urllib,sys,time
import cookielib,mechanize
import re
DEBUG =0
reload(sys) 
sys.setdefaultencoding('utf8') #@UndefinedVariable

register_openers()

headers = {
           'Host':'esf.soufun.com',           
           'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1: SV1)',
           #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           #'Accept-Language':'zh-cn,zh;q=0.5',
           #'Accept-Encoding':'gzip, deflate',
           #'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7',
           'Keep-Alive':'115',
           'Connection':'keep-alive',          
        
           
           }

#datagen11, headers = multipart_encode({"fileUploadInput": open("/home/myapp/Screenshot-1.jpg","rb"),"backFunction": "$.c.Uploader.finish"})

class httpPost():
    data = {}
    def __init__(self,dataDic):
        self.cookie = cookielib.CookieJar()
        
        httpsHandler = urllib2.HTTPHandler()        
        httpsHandler.set_http_debuglevel(DEBUG)        
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie),httpsHandler)        
        
        self.data = dataDic
        
    def login1(self):
        self.brow = mechanize.Browser()
        
        httpHandler = mechanize.HTTPHandler()
        httpsHandler = mechanize.HTTPSHandler()
        
        httpHandler.set_http_debuglevel(DEBUG)
        self.cookiejar = mechanize.LWPCookieJar()
        #self.cookiejar = "Cookie    lzstat_uv=34741959842666604402|1786789; Hm_lvt_976797cb85805d626fc5642aa5244ba0=1304534271541; ASPSESSIONIDQCDRAQBB=JHCHINLAHGMAIGBIFMNANLGF; lzstat_ss=2189193215_2_1304564199_1786789; Hm_lpvt_976797cb85805d626fc5642aa5244ba0=1304535401191"
        self.opener = mechanize.OpenerFactory(mechanize.SeekableResponseOpener).build_opener(
                                        httpHandler,httpsHandler,
                                        mechanize.HTTPCookieProcessor(self.cookiejar),
                                        mechanize.HTTPRefererProcessor,
                                        mechanize.HTTPEquivProcessor,
                                        mechanize.HTTPRefreshProcessor,
                                        )
        self.opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"),
                             ("From", "")]
        #self.opener.addheaders = [(
         #                     "Referer", self.data['postUrl']
        #                      )]
        login={}
        login['method'] = self.data['method']
        login['name'] = self.data['name']
        login['pwd'] = self.data['pwd']
        loginUrl = self.data['loginUrl']+'?'+urllib.urlencode(login)
        print loginUrl
        response = mechanize.urlopen("http://esf.soufun.com/")
        response = mechanize.urlopen(loginUrl)
        print response.read().decode('gb2312')
        
    def login(self):
        br = mechanize.Browser()
        
        self.cookie = cookielib.CookieJar()
        httpsHandler = urllib2.HTTPHandler()        
        httpsHandler.set_http_debuglevel(DEBUG)        
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie),httpsHandler)
        self.opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13"),
                             ("From", "")]
        login={}
        login['method'] = self.data['method']
        login['name'] = self.data['name']
        login['pwd'] = self.data['pwd']
        loginUrl = self.data['loginUrl']        
        req = urllib2.Request(loginUrl,urllib.urlencode(login))
        r =     self.opener.open(req)
        print r.read()
        for item in self.cookie:
            print item.name,item.value
        req = urllib2.Request('http://agent0.soufun.com/magent/main.aspx')
        print self.opener.open(req).read().decode('gb2312')
        #open('login.txt','w').write(r.read().encode('utf-8'))
        
    def post(self):
        pass
    
    
postData = {}
postData['loginUrl'] = 'http://esf.soufun.com/newsecond/include/DefaultUserLoginNew.aspx'
postData['method'] = 'login'
postData['name'] = 'ksjy02'
postData['pwd'] = '513310'
http = httpPost(postData)
http.login()
