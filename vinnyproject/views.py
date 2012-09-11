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


import uuid

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from socialregistration.contrib.facebook.models import FacebookProfile

# TODO: review to remove socialregistration or not
#       review to reuse the setup (callback) or not
@csrf_exempt
@ajax_required
@require_POST
def facebook_connect(request):
    """
    Create or get user from Facebook auth response

        authResponse = {
            accessToken: string,
            expiresIn: number,
            signedRequest: string,
            userID: string
        }
    """

    # TODO: verify request.POST

    profile, created  = FacebookProfile.objects.get_or_create(
                            uid=request.POST['userID'],
                            site=Site.objects.get_current(),
                            defaults={
                                'user': User.objects.create(username=uuid.uuid4().hex[:30])
                            })

    data = {
        'username': profile.user.username,
        'status': "new" if created else "exist",
    }

    # TODO: check whether the FacebookAccessToken created or not

    return HttpResponse(json.dumps(data), content_type="application/json")
