import json

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.template import RequestContext
from django.conf import settings


# From http://djangosnippets.org/snippets/771/
def ajax_required(f):
    """
    AJAX request required decorator
    use it in your views:

    @ajax_required
    def my_view(request):
        ....

    """    
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

@ajax_required
def ajax_login(request, template_name='ajax_login.html'):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            data = { 
                "location": getattr(settings, "LOGIN_REDIRECT_URL", "/"),
            }   
        else:
            data = {
                "html": render_to_string(template_name, {'form': form}, RequestContext(request)),
            }
    else:
        form = AuthenticationForm(request)
        data = {
            "html": render_to_string(template_name, {'form': form}, RequestContext(request)),
        }
    return HttpResponse(json.dumps(data), content_type="application/json")
