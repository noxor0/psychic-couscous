from math import radians, sin, cos, sqrt, atan2
from Database import Database

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
        all_hikes = db.get_hikes()

        # find hikes within 80 miles
        for hike in all_hikes:
            if(self.find_distance(user.lat, user.lng, hike.lat, hike.lng) < 50):
                if(abs(user.skill - hike.difficulty) <= 1.5):
                    poss_hikes.append([hike, abs(user.skill - hike.difficulty)])

        freq_table = db.get_hike_frequency()
        freq_table = list(freq_table)
        freq_table.sort(key=lambda x: x[1], reverse=True)
        print freq_table
        print poss_hikes
        # for hike1 in poss_hikes:
        #     print hike1[0].name

        if(len(poss_hikes) < 3):
            return "no hikes!"
        poss_hikes.sort(key=lambda x: x[1])
        for i in range(3):
            top_three.append(poss_hikes[i][0])
        return top_three

db = Database()
hb = HikeBuddy()
suggestions = hb.find_suggestions()
db.close()
# for sugg in suggestions:
#     print sugg.name

# cool distance works
# print hb.find_distance(47.1152, -122.2917, 47.4017, -121.3736)
