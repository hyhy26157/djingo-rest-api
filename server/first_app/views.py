from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

def index(request): #request convection language
    return render(request,'index.html')

def user_page(request):
    context = {'Name':'Darius'}
    return render(request,'user_page.html', context = context)

def help1(request):
    Webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': Webpage_list}
    topic_list = Topic.objects.all()
    topic_dict = {'topics': topic_list}
    combined_dict = {**date_dict, **topic_dict}
    return render(request, 'help1.html', context = combined_dict)

# Create your views here.
