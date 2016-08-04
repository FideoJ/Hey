__author__ = 'Lin Jian' 
# -*- coding: utf-8 -*-
import urllib2
import re
import sys

def get_page(page_index, filename):
    page_url = 'http://www.stjszx.net/jszxgk/gk.asp?page=' + str(page_index)
    try:
        #headers = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'}
        request = urllib2.Request(page_url)
        response = urllib2.urlopen(request, timeout = 10)
        print 'Page {0}: Connected'.format(page_index)
    except urllib2.URLError, e:
        print 'Page {0}: {1}. Retry!'.format(page_index, e.reason)
        #exit()
        return False

    #lines = response.readlines()
    #valid_lines = lines[1056:]
    #content = ''.join(valid_lines).decode('gbk')

    content = u''
    for i, line in enumerate(response):
        if i > 1090:
            content += line.decode('gbk')
    #print 'Page {0}: Loaded'.format(page_index)

    pattern = re.compile(r'<tr>[\s ]*<td><div align="center">(?P<ID>\d+)</div></td>[\s ]*<td><div align="center">(?P<Name>.*?)</div></td>[\s ]*<td><div align="center">(?P<College>.*?)</div></td>[\s ]*<td><div align="center">(?P<Major>.*?)</div></td>[\s ]*<td><div align="center">(?P<ArriveDate>.*?)&nbsp;</div></td>[\s ]*<td><div align="center">(?P<ArriveID>.*?)&nbsp;</div></td>[\s ]*</tr>', re.S)
    persons = re.findall(pattern, content)
    #print 'Page {0}: Found'.format(page_index)
    
    with open(filename, 'a') as f:
        for person in persons:
            for item in person:
                f.write(u'{0:15}'.format(item).encode('utf-8'))
            f.write(u'\n'.encode('utf-8'))
    print 'Page {0}: Done'.format(page_index)
    return True


for page_index in range(1,12):
    while (get_page(page_index, sys.argv[1]) == False):
        pass
