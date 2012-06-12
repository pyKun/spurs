from django.shortcuts import render_to_response
from django.http import HttpResponse

def google(request):
    return render_to_response('google.html', {})

def dbg(request):
    user = request.GET.get('screen_name')
    from apps.conn.twitter import retweeted_to_user as api
    hk = api(screen_name = user, count='4')
    hk.process()
    return HttpResponse(hk.response)

def search(request):
    #import ipdb;ipdb.set_trace()
    return render_to_response('search.html', {})
