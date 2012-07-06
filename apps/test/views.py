from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

import copy, json, time


sina_access_token = None

def google(request):
    return render_to_response('google.html', {})

def dbg(request):
    user = request.GET.get('screen_name')
    from apps.conn.twitter import retweeted_to_user as api
    hk = api(screen_name = user, count='4')
    hk.process()
    return HttpResponse(hk.response)

def search(request):
    return render_to_response('search.html', {}, context_instance=RequestContext(request))

def test(request):
    url = 'https://api.weibo.com/oauth2/authorize?client_id=1126538078&redirect_uri=http://127.0.0.1:8000/token/&response_type=token&display=popup'
    return HttpResponseRedirect(url)

def account_test_page(request):
    global sina_access_token
    hk = {'name':'huangkun'}
    sina = {'name':'sina','url':'https://api.weibo.com/oauth2/authorize?client_id=1126538078&redirect_uri=http://127.0.0.1:8000/token/&response_type=token','token':sina_access_token}
    twitter = {'name':'twitter','url':'#','token':'not supported'}
    tweepy = {'name':'tweepy','url':'#','token':'not supported'}
    data = {'users':[hk],
            'apis':[sina, twitter, tweepy]}
    return render_to_response('account_test.html', data, context_instance=RequestContext(request))

def update_sina_msg():
    global sina_access_token
    from apps.conn.sina import user_timeline as api
    rq = api(screen_name='',count='5',access_token=sina_access_token)
    rq.process()
    return rq.response
def update_twitter_msg():
    from apps.conn.twitter import user_timeline as api
    rq = api(count='5')
    rq.process()
    return rq.response
def update_tweepy_msg():
    from apps import tweepy
    from apps.conn.twitter import twitter_setting
    t = copy.deepcopy(twitter_setting)
    auth = tweepy.OAuthHandler(t['oauth_consumer_key'], t['consumer_secret'])
    auth.set_access_token(t['oauth_token'], t['token_secret'])

    api = tweepy.API(auth)
    newest = [i.text for i in api.user_timeline(count=5)]
    return newest

def dbg2(request):
    msg = request.GET.get('msg')
    api = request.GET.get('api')
    if api == 'all':
        r = update_by_all(msg + ' by Spurs')
    elif api == 'twitter':
        r = update_by_twitter(msg + ' By Spurs-tw')
    elif api =='sina':
        r = update_by_sina(msg + ' By Spurs-sina')
    elif api == 'tweepy':
        r = update_by_tweepy(msg + ' By Spurs-twe')
        r = json.dumps([{'user':{'screen_name':r['name']},'text':msg}for msg in r['msg']])

    if r:
        return HttpResponse(r)
    else:
        return HttpResponse('errors happen')

def update_by_sina(msg):
    # update status
    from apps.conn.sina import sina_update
    update = sina_update(access_token=sina_access_token, status=msg)
    update.process()

    # update board
    newest = update_sina_msg()
    return newest

def update_by_twitter(msg):
    # update status
    from apps.conn.twitter import update as api
    update = api(status=msg)
    update.process()

    # update board
    time.sleep(3)
    newest = update_twitter_msg()
    return newest

def update_by_tweepy(msg):
    from apps import tweepy
    from apps.conn.twitter import twitter_setting
    t = copy.deepcopy(twitter_setting)
    auth = tweepy.OAuthHandler(t['oauth_consumer_key'], t['consumer_secret'])
    auth.set_access_token(t['oauth_token'], t['token_secret'])

    api = tweepy.API(auth)
    me = api.me().screen_name
    # update status
    api.update_status(status=msg)

    # update board
    time.sleep(2)
    newest = update_tweepy_msg()
    return {'name':me, 'msg':newest}

def update_by_all(msg):
    # update all boards
    sina = update_by_sina(msg)
    twitter = update_by_twitter(msg)
    #tweepy = update_by_tweepy(msg)
    tweepy = twitter
    r = json.dumps({'sina':json.loads(sina),
                    'twitter':json.loads(twitter),
                    'tweepy':json.loads(tweepy)})
    return r

def token(request):
    data = {}
    return render_to_response('token.html', data)

def update(request):
    access_token = request.GET.get('access_token')
    global sina_access_token
    sina_access_token = access_token
    return HttpResponse('')
