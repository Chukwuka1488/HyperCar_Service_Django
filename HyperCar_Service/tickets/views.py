from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')
