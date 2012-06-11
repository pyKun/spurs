from conn import GET, urlopen
# TODO implement post

_fmt = lambda data : 'json' if data.pop('format','json') == 'json' else 'xml'

_drag = lambda data, table : { key:data.pop(key) for key in table if key in data }

class retweeted_to_user(object):
    '''
    GET statuses/retweeted_to_user

    Document URL:
        https://dev.twitter.com/docs/api/1/get/statuses/retweeted_to_user

    Resource URL:
        http://api.twitter.com/1/statuses/retweeted_to_user.format

    Description:
        Returns the 20 most recent retweets posted by users the specified user follows.
        The user is specified using the user_id or screen_name parameters. This method is
        identical to statuses/retweeted_to_me except you can choose the user to view.
    '''
    def __init__(self, **kwargs):
        url = "http://api.twitter.com/1/statuses/retweeted_to_user.%s" % _fmt(kwargs)
        self.params_table = ('screen_name',
                             'id',
                             'count',
                             'since_id',
                             'max_id',
                             'page',
                             'trim_user',
                             'include_entities')
        params = _drag(data=kwargs, table=self.params_table)

        if kwargs:
            # TODO use log
            print "warning: there's excess key-word arguments: ", kwargs

        self.request = GET(url, params)
        #self.process()

    def process(self):
        try:
            response = urlopen(self.request)
        except Exception as e :
            import ipdb;ipdb.set_trace()
        self.response = response.read()
