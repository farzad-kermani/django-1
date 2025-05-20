from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def home_page(request):
#     return render(request,'pages\home.html',{})

class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    
class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
        
    