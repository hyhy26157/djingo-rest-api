from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from first_app import serializer


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to the URLs',

        ]

        return Response({'message':'hello','an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello msg in our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        """Handle updating an objects"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method":'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete  an object"""
        return Response({'method':"DELETE"})


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
