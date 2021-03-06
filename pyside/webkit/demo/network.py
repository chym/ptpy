'''
Created on Jan 22, 2013

@author: joseph

http://www.cnblogs.com/huys03/archive/2012/09/02/2667475.html
'''
from PySide import QtGui
from PySide import QtCore
from PySide import QtWebKit,QtNetwork
from PySide.QtNetwork import QNetworkRequest,QNetworkAccessManager,QNetworkReply
import os
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


def serverStart():    
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    server_address = ('127.0.0.1', 8000)
    HandlerClass.protocol_version = "HTTP/1.0"
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    httpd.serve_forever()

class ConsolePrinter(QtCore.QObject):
    def __init__(self,parent = None):
        super(ConsolePrinter,self).__init__(parent)
        
    @QtCore.Slot(str)
    def text(self,msg):
        print msg   
   
class NetwordAccMan(QtNetwork.QNetworkAccessManager):
    def __init__(self):   
        QtNetwork.QNetworkAccessManager.__init__(self)
        '''
        def finished (reply)
        def networkAccessibleChanged (accessible)
        def networkSessionConnected ()
        '''
        self.finished.connect(self.finishe)
        self.networkAccessibleChanged.connect(self.networkAccessibleChange)
        self.networkSessionConnected.connect(self.networkSessionConnect)    
    
    def createRequest(self, operation, request, data):
        # data contains all the post data that is being added to the request
        # so you can look into it here
        #print "replay:====>",request.url().toString(),operation     
        #url = request.url().toString()   
        reply = QNetworkAccessManager.createRequest(self, operation,request,data)      
        #if "js" in url or "gif" in url:
            #reply = QNetworkAccessManager.createRequest(self,QNetworkAccessManager.GetOperation,QNetworkRequest(QtCore.QUrl("")))  
            #reply = QNetworkAccessManager.createRequest(self, operation,request,data)        
        #else:                                           
        return reply
        
    def finishe(self,reply):
        pass#print reply.url()        
        pass#print reply.request()
    def networkAccessibleChange(self,accessible):
        pass#print "accessible",accessible
    def networkSessionConnect(self):
        pass#print "networkSessionConnect"
    
class WebPage(QtWebKit.QWebPage):
    def __init__(self):
        QtWebKit.QWebPage.__init__(self)
        self.frame = frame = self.mainFrame()     
        printer = ConsolePrinter()       
        frame.addToJavaScriptWindowObject('printer',printer)
        
        #frame.evaluateJavaScript("alert(\"hello world\")")
        #self.setContentEditable(True)
        self.setNetworkAccessManager(NetwordAccMan())
        self.linkHovered.connect(self.linkHover)
        self.statusBarMessage.connect(self.statusBarMsg)
        self.loadFinished.connect(self.loadFinish)
        self.loadStarted.connect(self.loadStart)
        self.loadProgress.connect(self.Progress)
        self.selectionChanged.connect(self.selectionChange)
        self.linkClicked.connect(self.linkClick)
        
    def linkClick(self,url):
        pass#print url     
    def selectionChange(self):
        pass#print self.selectedText()
    def Progress(self,progress):
        print progress
    def loadStart(self):
        pass
        #print "start", self.frame.url().toString()
    def loadFinish(self):
        pass#print "finished", self.frame.url().toString()
        #print self.frame.icon()
        #print self.frame.metaData()
        #print self.networkAccessManager().cookieJar().allCookies()
        
    def statusBarMsg(self,msg):
        pass#print "status bar msg",msg
    def linkHover(self,link, title, textContent):
        pass#print link, title, textContent
    def userAgentForUrl(self, url):
        return "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15"


class WebView(QtWebKit.QWebView):
    def __init__(self,parent = None):
        QtWebKit.QWebView.__init__(self,parent)     
        self.settings().setAttribute(
            QtWebKit.QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
        
        self.setPage(WebPage())
        self.titleChanged.connect(self.titleChange)   
        self.urlChanged.connect(self.urlChange)
        
    def titleChange(self,title):
        print title
    def urlChange(self,url):
        print url   

class Browser(QtGui.QMainWindow):
    def __init__(self,url):
        QtGui.QMainWindow.__init__(self) 
        
        webview = WebView(self)
        self.setCentralWidget(webview)
        webview.load(QtCore.QUrl(url))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    browser = Browser("http://www.baidu.com/")       
    
    browser.show()
    sys.exit(app.exec_())