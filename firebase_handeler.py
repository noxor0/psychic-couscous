from firebase import firebase
from HikeBuddy import HikeBuddy

def post_new(self):
    hb = HikeBuddy()
    suggestions = hb.find_suggestions()
    firebase1 = firebase.FirebaseApplication('https://hikeaway-6b0f0.firebaseio.com/', None)
    firebase1.put('/', 'suggestion', data=suggestions)


 post_new()
print firebase1.get('/suggestion', None)
