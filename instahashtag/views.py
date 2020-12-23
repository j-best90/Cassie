from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,template_name='base.html')

def ugc_tracker(request):
    return render(request,template_name='ugc_tracker.html')

