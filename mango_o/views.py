from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Me'h yega be'h Oooh... Index djem ini'h.")
