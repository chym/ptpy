'''
Created on Oct 20, 2012

@author: joseph
'''
#http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html
from BeautifulSoup import BeautifulSoup
import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']

soup = BeautifulSoup(''.join(doc))
print soup.prettify()
print soup.contents[0].name
print soup.contents[0].contents[0].name