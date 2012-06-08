from django.shortcuts import render_to_response
#from django.http import HttpResponse

def search(request):
    return render_to_response('search.html', {})
