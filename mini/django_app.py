from django.conf.urls import url
from django.http import HttpResponse

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__

def hello(request):
    return HttpResponse('Hello, World!')

urlpatterns = [
    url(r'^$', hello),
]