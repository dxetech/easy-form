import json
from boto import ses
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from easyform.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY
from .models import Key

# Create your views here.
def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = json.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator

@json_response
def home(request):
    return {"message" : "index"}

@json_response
def mailer(request):
    api_key = request.REQUEST.get("api_key", "")
    key = get_object_or_404(Key, api_key=api_key)

    for k in ["name", "email", "subject", "body", "to_addresses"]:
        if k not in request.REQUEST:
            return {'message' : 'ERROR, param %s missing' % k}
    connection = ses.connection.SESConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)
    body = "Email From: %s, %s \n%s" % (request.REQUEST["name"],
            request.REQUEST["email"], request.REQUEST["body"])
    email_context = {
        "source" : "james@dxetech.com",
        "subject" : request.REQUEST["subject"],
        "body" : body,
        "to_addresses" : request.REQUEST["to_addresses"]
        }
    connection.send_email(**email_context)
    return {'message' : 'successful'}
