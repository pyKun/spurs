from conn import GET, urlopen, POST
import copy, time, json, random
from urllib import quote, unquote

q = lambda s : quote(s, safe='')

_fmt = lambda data : 'json' if data.pop('format','json') == 'json' else 'xml'

_drag = lambda data, table : { key:q(data.pop(key)) for key in table if key in data }

twitter_setting = {'oauth_consumer_key':'tXNzsla1b609W3w5lytRA',
                   'oauth_nonce':None,
                   'oauth_signature':None,
                   'oauth_signature_method':'HMAC-SHA1',
                   'oauth_timestamp':None,
                   'oauth_token':'593651382-RhxpHzUoijOTmE4DUehQP7Qmggp9PA7EDTUt40SY',
                   'oauth_version':'1.0',
                   'consumer_secret':'krrpvHoogodzS7LCJaAa5VJy1Y9o3ZoD1imkaqEifY',
                   'token_secret':'nji7AnWjt3GDZrqCMz3PDT63XepGsGaA2VFq6LPCAQ'}

class base_api(object):
    def get_signature(self, url, method):
        # from http://stackoverflow.com/questions/8338661/implementaion-hmac-sha1-in-python
        from hashlib import sha1
        import hmac
        import binascii

        _key = self.ts.pop('consumer_secret') + '&' + self.ts.pop('token_secret')

        temp = [q(key)+'='+q(value) for key, value in copy.deepcopy(self.ts).iteritems() if value]
        temp.extend([q(key)+'='+q(value) for key, value in self.params.iteritems() if value])
        parameter_string = '&'.join(sorted(temp))
        raw = '&'.join([method,q(url),q(parameter_string)])

        hashed = hmac.new(_key, raw, sha1)
        return binascii.b2a_base64(hashed.digest())[:-1]

    def get_authorization_header(self, url, method):
        self.ts = copy.deepcopy(twitter_setting)
        self.ts['oauth_timestamp'] = str(int(time.time()))
        self.ts['oauth_nonce'] = ''.join([str(random.randint(0, 9)) for i in range(9)])
        self.ts['oauth_signature'] = self.get_signature(url, method)

        dst = 'OAuth ' + ', '.join(sorted('%s="%s"' %(key, q(value)) for key, value in self.ts.iteritems()))
        return dst

    def process(self):
        try:
            response = urlopen(self.request)
        except Exception as e :
            import ipdb;ipdb.set_trace()
            self.response = json.dumps(json.loads(e.read()))
            print "LOG: ", "warning: errors happens: %s" % self.response
        else:
            self.response = response.read()


class retweeted_to_user(base_api):
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
            # TODO  use log
            print "LOG: ", "warning: there's excess key-word arguments: ", kwargs

        self.request = GET(url, params)


class update(base_api):
    '''
    POST statuses/update

    Document URL:
        https://dev.twitter.com/docs/api/1/post/statuses/update

    Resource URL:
        http://api.twitter.com/1/statuses/update.format

    Description:
        Updates the authenticating user's status, also known as tweeting. To upload an
        image to accompany the tweet, use POST statuses/update_with_media.

        For each update attempt, the update text is compared with the authenticating
        user's recent tweets. Any attempt that would result in duplication will be
        blocked, resulting in a 403 error. Therefore, a user cannot submit the same
        status twice in a row.

        While not rate limited by the API a user is limited in the number of tweets they
        can create at a time. If the number of updates posted by the user reaches the
        current allowed limit this method will return an HTTP 403 error.
    '''
    def __init__(self, **kwargs):
        url = "https://api.twitter.com/1/statuses/update.%s" % _fmt(kwargs)
        self.params_table = ('status',)
        self.params = _drag(data=kwargs, table=self.params_table)

        if kwargs:
            # TODO use log
            print "LOG: ", "warning: there's excess key-word arguments: ", kwargs
        headers = self.get_authorization_header(url, 'POST')
        self.request = POST(url, self.params, headers={'Authorization':headers})


class user_timeline(base_api):
    '''
    POST statuses/home_timeline

    Document URL:
        https://dev.twitter.com/docs/api/1/get/statuses/user_timeline

    Resource URL:
        http://api.twitter.com/1/statuses/user_timeline.format

    Description:
        Returns the most recent statuses, including retweets if they exist, posted by
        the authenticating user and the users they follow. This is the same timeline
        seen by a user when they login to twitter.com.

        This method is identical to statuses/friends_timeline, except that this method
        always includes retweets.

        This method is can only return up to 800 statuses, including retweets, across
        all pages.

        See Working with Timelines for instructions on traversing timelines.
    '''
    def __init__(self, **kwargs):
        url = "http://api.twitter.com/1/statuses/user_timeline.%s" % _fmt(kwargs)
        self.params_table = ('count',)
        self.params = _drag(data=kwargs, table=self.params_table)

        if kwargs:
            # TODO use log
            print "LOG: ", "warning: there's excess key-word arguments: ", kwargs
        headers = self.get_authorization_header(url, 'GET')
        self.request = GET(url, self.params, headers={'Authorization':headers})
