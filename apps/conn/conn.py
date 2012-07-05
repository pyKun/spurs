from urllib2 import *
from urllib import urlencode

protocol = ('http', 'https', 'ftp', 'socks')
goagent = '127.0.0.1:8087'

proxy = ProxyHandler(dict.fromkeys(protocol, goagent))
opener = build_opener(HTTPHandler, HTTPSHandler, proxy)
opener.addheaders = [('Accept-Encoding', '')]
install_opener(opener)

direct_opener = build_opener(HTTPHandler, HTTPSHandler)
direct_opener.addheaders = [('Accept-Encoding', '')]

class GET(Request):
    def __init__(self, url, params=None, **kwargs):
        if params:
            self.url = url + '?' + urlencode(params)
        else:
            self.url = url
        print 'GET ', self.url
        Request.__init__(self, self.url, **kwargs)

class POST(Request):
    def __init__(self, url, params=None, **kwargs):
        self.url = url
        data = urlencode(params)
        print 'POST ', self.url, data
        Request.__init__(self, self.url, data=data, **kwargs)
