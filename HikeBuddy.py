from math import radians, sin, cos, sqrt, atan2
from Database import Database
import json

class HikeBuddy(object):
# 1 degree of Longitude =
# cosine (latitude in decimal degrees) * length of degree (miles) at equator.
    def find_distance(self, user_lat, user_long, trail_lat, trail_long):
        R = 6373.0
        lat1 = radians(user_lat)
        lon1 = radians(user_long)
        lat2 = radians(trail_lat)
        lon2 = radians(trail_long)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        distance = distance * .621371
        return distance

    def decimal_default(object):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        raise TypeError

    def find_suggestions(self):
        poss_hikes = []
        top_three = []

        user = db.get_user(1)
        all_hikes = db.get_hikes()

        # find hikes within 80 miles
        for hike in all_hikes:
            if(self.find_distance(user.lat, user.lng, hike.lat, hike.lng) < 50):
                if(abs(user.skill - hike.difficulty) <= 1.5):
                    poss_hikes.append([hike, abs(user.skill - hike.difficulty)])

        if(len(poss_hikes) < 3):
            return "no hikes!"
        poss_hikes.sort(key=lambda x: x[1])
        for i in range(3):
            temp = {}
            temp['trailID'] = poss_hikes[i][0].trail_id
            temp['name'] = poss_hikes[i][0].name
            temp['difficulty'] = str(poss_hikes[i][0].difficulty)
            temp['lat'] = str(poss_hikes[i][0].lat)
            temp['lng'] = str(poss_hikes[i][0].lng)
            temp = json.dumps(temp)
            top_three.append(temp)
        return top_three

db = Database()
hb = HikeBuddy()
suggestions = hb.find_suggestions()
# print suggestions
db.close()
