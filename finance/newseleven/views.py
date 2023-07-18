from django.shortcuts import render
# step 1.1 import HttpResponse 
from django.http import HttpResponse

from .models import News
# step 1.2 create function with request parameter
# index is function name
def index(request):
    # step 1.3 return content with HttpResponse
    return HttpResponse("News Eleven -> index")

def home_page(request):
    news_list = News.objects.all()
    return render(request, 'news_home_page.html',{'news_list' :  news_list})

def our_home_page(request):
    return render(request, 'our_html.html')