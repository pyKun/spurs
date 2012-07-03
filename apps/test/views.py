from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def google(request):
    return render_to_response('google.html', {})

def dbg(request):
    user = request.GET.get('screen_name')
    from apps.conn.twitter import retweeted_to_user as api
    hk = api(screen_name = user, count='4')
    ############################################################
    if False:
        from apps import tweepy
        consumer_key="tXNzsla1b609W3w5lytRA"
        consumer_secret="krrpvHoogodzS7LCJaAa5VJy1Y9o3ZoD1imkaqEifY"

        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located
        # under "Your access token")
        access_token="593651382-LFxkIMyhdLmQxavB6XRS7CRVirs53jwqv1WLO1K0"
        access_token_secret="9vmIOKybQnPvFmUY2UGSbAdu9GWNXCRRb5oxQTZBQ"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        print api.me().name
        import ipdb;ipdb.set_trace()
    #############################################################
    hk.process()
    return HttpResponse(hk.response)

def search(request):
    #import ipdb;ipdb.set_trace()
    return render_to_response('search.html', {}, context_instance=RequestContext(request))

def test(request):
    from apps.conn.conn import urlopen, GET
    from apps import tweepy
    consumer_key="tXNzsla1b609W3w5lytRA"
    consumer_secret="krrpvHoogodzS7LCJaAa5VJy1Y9o3ZoD1imkaqEifY"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    import ipdb;ipdb.set_trace()
    url = 'https://api.weibo.com/oauth2/authorize?client_id=1126538078&redirect_uri=http://127.0.0.1:8000&response_type=token&display=popup'
    req = GET(url, {})
    respone = urlopen(req)
    return HttpResponseRedirect(url)

def account_test_page(request):
    hk = {'name':'huangkun'}
    sina = {'name':'sina'}
    twitter = {'name':'twitter'}
    tweepy = {'name':'tweepy'}
    data = {'users':[hk],
            'apis':[sina, twitter, tweepy]}
    return render_to_response('account_test.html', data, context_instance=RequestContext(request))

def dbg2(request):
    msg = request.GET.get('msg')
    api = request.GET.get('api')
    if api == 'all':
        r = update_by_all()
    elif api == 'twitter':
        r = update_by_twitter()
    elif api =='sina':
        r = update_by_sina()
    elif api == 'tweepy':
        r = update_by_tweepy()

    if r == True:
        return HttpResponse('update %s by %s' % (msg,api))
    else:
        return HttpResponse('errors happen')

def update_by_sina():
    return

def update_by_twitter():
    return

def update_by_tweepy():
    return

def update_by_all():
    return
