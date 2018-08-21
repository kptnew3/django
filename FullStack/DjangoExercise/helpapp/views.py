from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def funchelpapp(request):
    dictHelp = {
        "help_by_django":"Django is helping me running website",
    }
    return render(request,'helpapp/index.html',context=dictHelp)
