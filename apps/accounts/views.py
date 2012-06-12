from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.middleware.csrf import get_token

def do_login(request):
    data = request.POST
    name = data.get('name')
    pw = data.get('pw')
    user = authenticate(username=name, password=pw)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/test/search/')
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        pass

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/test/search/')

def login_page(request): # login page
    get_token(request)
    return render_to_response('login.html', {}, context_instance=RequestContext(request))
