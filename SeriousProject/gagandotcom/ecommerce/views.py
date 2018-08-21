from django.template.loader import get_template
from django.shortcuts import * 
# render_to_response, render, RequestContext
from django.template import Context
#from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import Context
from ecommerce.forms.login import LoginForm

import os

# Create your views here.
def index(request):

    # if 'firstname' in request.POST:
    
    if request.method == 'GET':
        # print("GET Request fired")
        # return render_to_response ('index.html', {'form_submitted': 'Accessed first time'}, RequestContext(request))
        #how to catch csrf token
        if 'csrfmiddlewaretoken' in request.GET:
            print("csrf token is " + request.GET['csrfmiddlewaretoken'])
        
        print('received GET Request without CSRF')

        form = LoginForm()

        return render(request, 'index.html', {'form_submitted': 'Accessed first time',
                                             'form': form})

    if request.method == 'POST':

        # print("POST request fired")
        
        # if request.FILES['file']:
        if 'csrfmiddlewaretoken' in request.POST:
            print("csrf token is " + request.POST['csrfmiddlewaretoken'])
 
        if request.FILES:

            file = request.FILES['file']
            filename=str(request.FILES['file'])

            if not os.path.exists('upload/'):
                os.mkdir('upload/')

            with open('upload/' + filename, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        
        print(request.POST['email'])
        print(request.POST['firstname'])
        print(request.POST['lastname'])
        # return render_to_response ('index.html', RequestContext(request, {'form_submitted': request.POST['firstname']}, RequestContext(request)))
        return render(request, 'index.html', {'form_submitted': request.POST['firstname']})

        

    # firstname = request.POST['firstname']
    # print(firstname)
    
    #     if firstname == "": 
    #         return render_to_response ('index.html', {'form_submitted': request.POST['firstname']})'
    #     else:
    #         return render_to_response ('index.html', {'form_submitted': 'firstname'})
    # else:
    #     return render_to_response ('index.html', {'form_submitted': 'sent the form'})

def form_submitted(request):
    #c = Context({'form_submitted' : "yes" })
    print(request.path)
    return render_to_response ('index.html', {'form_submitted' : 'goal' })
    


