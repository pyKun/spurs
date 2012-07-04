# -*- coding:utf-8 -*-
from conn import GET, urlopen, POST
import json

_drag = lambda data, table : { key:data.pop(key) for key in table if key in data }

class base_api(object):
    pass

class user_timeline(base_api):
    '''
    GET statuses/user_timeline

    Document URL:
        http://open.weibo.com/wiki/2/statuses/user_timeline

    Resource URL:
        https://api.weibo.com/2/statuses/user_timeline.json

    Description:
        获取某个用户最新发表的微博
    '''
    def __init__(self, **kwargs):
        url = "https://api.weibo.com/2/statuses/user_timeline.json"
        self.params_table = ('access_token',
                             'screen_name',
                             'count',)
        params = _drag(data=kwargs, table=self.params_table)
        if kwargs:
            # TODO use log
            print "LOG: ", "warning: there's excess key-word arguments: ", kwargs

        self.request = GET(url, params)

    def process(self):
        try:
            response = urlopen(self.request)
        except Exception as e :
            self.response = json.dumps(json.loads(e.read()))
            print "LOG: ", "warning: errors happens: %s" % self.response
        else:
            self.response = response.read()

class sina_update(base_api):
    '''
    POST  2/statuses/update

    Document URL:
        http://open.weibo.com/wiki/2/statuses/update

    Resource URL:
        https://api.weibo.com/2/statuses/update.json

    Description:
        发布一条微博
    '''
    def __init__(self, **kwargs):
        url = "https://api.weibo.com/2/statuses/update.json"
        self.params_table = ('access_token',
                             'status',)
        params = _drag(data=kwargs, table=self.params_table)
        if kwargs:
            # TODO use log
            print "LOG: ", "warning: there's excess key-word arguments: ", kwargs

        self.request = POST(url, params)

    def process(self):
        try:
            response = urlopen(self.request)
        except Exception as e :
            self.response = json.dumps(json.loads(e.read()))
            print "LOG: ", "warning: errors happens: %s" % self.response
        else:
            self.response = response.read()
