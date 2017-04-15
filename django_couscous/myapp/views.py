from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import Trail
from .models import User
from .models import UserHike
from firebase import firebase
from decimal import Decimal

# Create your views here.
def index(request):
    # name = 'Connor'
    # prev_hike1 = 'Ruston Way'
    # prev_hike2 = 'Chambers Bay'
    # context = {'user_name': name, 'pr_hike1': prev_hike1, 'pr_hike2': prev_hike2}

    # return render(request, 'index.html', context)
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    # userhike = UserHike.objects.get(userid=2) #TODO don't use get!!!
    context = {'user': user, 'skill': skill}#, 'userhike': userhike}
    return render(request, 'index.html', context)

# def suggest(request):
#     firebase1 = firebase.FirebaseApplication('https://hikeaway-6b0f0.firebaseio.com/', None)
#     suggestions = firebase1.get('/suggestion', None)
#     easy = suggestions[0]['name']
#     med = suggestions[1]['name']
#     hard = suggestions[2]['name']
#     context = {'easy': easy, 'med': med, 'hard': hard}
#     return render(request, 'suggest.html', context)
