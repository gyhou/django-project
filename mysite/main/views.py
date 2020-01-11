from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.
def homepage(request):
    # return HttpResponse("<strong>Django</strong> project")
    return render(request=request,
                  template_name='main/home.html',
                  context={'tutorials':Tutorial.objects.all})