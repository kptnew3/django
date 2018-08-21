from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(request):
    my_dict = {
        "insert_me":"<em>My First App</em>"
    }
    return render(request, 'DjangoExerciseApp/index.html', context=my_dict)
