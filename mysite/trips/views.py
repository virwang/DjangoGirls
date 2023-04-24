from datetime import datetime
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post,Trip,Activity


# 靜態版，no css etc
# def hello_world(request):
#     return HttpResponse("Hello World!")


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
        'Now': str(datetime.now()),
    })


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def post_detail(request, pk):
    print("pk: "+pk)
    return render(request, 'post.html', {
        'post':     Post.objects.get(pk=pk)
    })

def trip(request):
    trip = Trip.objects.all()
    return render(request,'trip.html',{'trip':trip})

def activity(request):
    activity = Activity.objects.all()
    return render(request,'activity.html',{'activity':activity})
