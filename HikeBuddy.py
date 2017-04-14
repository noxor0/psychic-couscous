from math import radians, sin, cos, sqrt, atan2
from Database import Database

#db.getHikes()
#db.getUser(userID)
db = Database()

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

    def find_suggestions(self):
        poss_hikes = []
        top_three = []

        user = db.get_user(1)
        local_hikes = db.get_hikes()

        # find hikes within 80 miles
        for hike in local_hikes:
            if(self.find_distance(user.lat, user.lng, hike.lat, hike.lng) < 80):
                if(abs(user.skill - hike.difficulty) <= 1.5):
                    poss_hikes.append([hike, abs(user.skill - hike.difficulty)])

        if(len(poss_hikes) < 3):
            return "no hikes!"
        poss_hikes.sort(key=lambda x: x[1])
        for i in range(3):
            top_three.append(poss_hikes[i][0])
        return top_three
