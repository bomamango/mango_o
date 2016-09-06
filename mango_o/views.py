from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Me'h yega be'h Oooh... Index djem ini'h. Allez plutot a --> <a href=>http://bomamango.pythonanywhere.com/blog/</a> --> copy/paste le lien ne waka pas ankor. Yia koi?")
