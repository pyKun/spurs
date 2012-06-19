from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def google(request):
    return render_to_response('google.html', {})

def dbg(request):
    user = request.GET.get('screen_name')
    from apps.conn.twitter import retweeted_to_user as api
    hk = api(screen_name = user, count='4')
    ############################################################
    if True:
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
