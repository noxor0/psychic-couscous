from firebase import firebase
from HikeBuddy import HikeBuddy
import threading

def post_new():
    hb = HikeBuddy()
    suggestions = hb.find_suggestions()
    firebase1 = firebase.FirebaseApplication('https://hikeaway-6b0f0.firebaseio.com/', None)
    result = firebase1.put('/', 'suggestion', data=suggestions)
    return result

def listen_change():
    firebase1 = firebase.FirebaseApplication('https://hikeaway-6b0f0.firebaseio.com/', None)
    return firebase1.get('/hike_response', None)

print listen_change()
# print post_new()
