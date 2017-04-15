from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    # name = 'Connor'
    # prev_hike1 = 'Ruston Way'
    # prev_hike2 = 'Chambers Bay'
    # context = {'user_name': name, 'pr_hike1': prev_hike1, 'pr_hike2': prev_hike2}

    # return render(request, 'index.html', context)
    user = User.objects.filter(userID=7)
    return render(request, 'index.html', {'user': user})
