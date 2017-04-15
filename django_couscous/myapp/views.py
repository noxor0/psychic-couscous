from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import Trail
from .models import User
from .models import UserHike
from firebase import firebase
from decimal import Decimal

firebase1 = firebase.FirebaseApplication('https://hikeaway-6b0f0.firebaseio.com/', None)
suggestions = firebase1.get('/suggestion', None)
# Create your views here.
# def index(request):
#     # return render(request, 'index.html', context)
#     user = User.objects.get(userid=1)
#     skill = user.skill * Decimal(10.0)
#     # userhike = UserHike.objects.get(userid=2) #TODO don't use get!!!
#     context = {'user': user, 'skill': skill}#, 'userhike': userhike}
#     return render(request, 'index.html', context)

def index1(request):
    response = [{'liked':-1, 'trailID':suggestions[0]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    # userhike = UserHike.objects.get(userid=2) #TODO don't use get!!!
    context = {'user': user, 'skill': skill}#, 'userhike': userhike}
    return render(request, 'index.html', context)

def index2(request):
    response = [{'liked':0, 'trailID':suggestions[1]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    # userhike = UserHike.objects.get(userid=2) #TODO don't use get!!!
    context = {'user': user, 'skill': skill}#, 'userhike': userhike}
    return render(request, 'index.html', context)

def index3(request):
    response = [{'liked':1, 'trailID':suggestions[2]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    # userhike = UserHike.objects.get(userid=2) #TODO don't use get!!!
    context = {'user': user, 'skill': skill}#, 'userhike': userhike}
    return render(request, 'index.html', context)

def suggest4(request):
    response = [{'liked':-1, 'trailID':suggestions[0]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    easy = suggestions[0]['name']
    med = suggestions[1]['name']
    hard = suggestions[2]['name']
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    context = {'easy': easy, 'med': med, 'hard': hard, 'skill': skill}
    return render(request, 'suggest.html', context)

def suggest5(request):
    response = [{'liked':0, 'trailID':suggestions[1]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    easy = suggestions[0]['name']
    med = suggestions[1]['name']
    hard = suggestions[2]['name']
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    context = {'easy': easy, 'med': med, 'hard': hard, 'skill': skill}
    return render(request, 'suggest.html', context)

def suggest6(request):
    response = [{'liked':1, 'trailID':suggestions[2]['trailID']}]
    firebase1.put('/', 'hike_response', data=response)
    easy = suggestions[0]['name']
    med = suggestions[1]['name']
    hard = suggestions[2]['name']
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    context = {'easy': easy, 'med': med, 'hard': hard, 'skill': skill}
    return render(request, 'suggest.html', context)

def suggest(request):
    suggestions = firebase1.get('/suggestion', None)
    easy = suggestions[0]['name']
    med = suggestions[1]['name']
    hard = suggestions[2]['name']
    user = User.objects.get(userid=1)
    skill = user.skill * Decimal(10.0)
    context = {'easy': easy, 'med': med, 'hard': hard, 'skill': skill}
    return render(request, 'suggest.html', context)
