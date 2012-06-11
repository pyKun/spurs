from django.shortcuts import render_to_response
from django.http import HttpResponse

def google(request):
    return render_to_response('google.html', {})

def dbg(request):
    from apps.conn.twitter import retweeted_to_user as api
    hk = api(screen_name = 'ctype2')
    hk.process()
    return HttpResponse(hk.response)

def search(request):
    return render_to_response('search.html', {})
